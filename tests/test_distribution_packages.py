import hashlib
import sys
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch
from zipfile import ZipFile

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))

import build_packages
import validate_packages


class DistributionTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.root = Path(temporary.name)
        self.output = self.root / "output"
        build_packages.build(self.output)

    def test_build_is_reproducible_and_validation_accepts_it(self):
        repeat = self.root / "repeat"
        build_packages.build(repeat)
        for file in self.output.iterdir():
            self.assertEqual(file.read_bytes(), (repeat / file.name).read_bytes(), file.name)
        validate_packages.validate(self.output)

    def test_cannot_overwrite_existing_output(self):
        marker = self.output / "SHA256SUMS"
        before = marker.read_bytes()
        with self.assertRaises(FileExistsError):
            build_packages.build(self.output)
        self.assertEqual(marker.read_bytes(), before)

    def test_interrupted_build_does_not_leave_a_candidate(self):
        interrupted = self.root / "interrupted"
        with patch.object(build_packages.ZipFile, "writestr", side_effect=OSError("disk error")):
            with self.assertRaisesRegex(OSError, "disk error"):
                build_packages.build(interrupted)
        self.assertFalse(interrupted.exists())

    def test_rejects_tampered_checksums(self):
        (self.output / "SHA256SUMS").write_text("unverified", encoding="ascii")
        with self.assertRaisesRegex(ValueError, "SHA256SUMS"):
            validate_packages.validate(self.output)

    def test_rejects_unexpected_members_even_with_recomputed_checksum(self):
        archive_path = self.output / "agent-assurance-community.zip"
        original_hash = hashlib.sha256(archive_path.read_bytes()).hexdigest()
        with ZipFile(archive_path, mode="a") as archive:
            archive.writestr("../outside.md", "unexpected")
        modified_hash = hashlib.sha256(archive_path.read_bytes()).hexdigest()
        sums = self.output / "SHA256SUMS"
        sums.write_bytes(sums.read_bytes().replace(original_hash.encode(), modified_hash.encode()))
        with self.assertRaisesRegex(ValueError, "unexpected, missing, or duplicate entries"):
            validate_packages.validate(self.output)
        self.assertFalse((self.root / "outside.md").exists())

    def test_rejects_reference_not_in_archive(self):
        read_file = build_packages.repository_file

        def invalid_skill(relative_path):
            data = read_file(relative_path)
            if relative_path == "skills/ai-pr-evidence-review/SKILL.md":
                return data + b"\n[Missing reference](references/missing.md)\n"
            return data

        with patch.object(build_packages, "repository_file", side_effect=invalid_skill):
            with self.assertRaisesRegex(ValueError, "unpackaged or external resource"):
                build_packages.build(self.root / "invalid")
        self.assertFalse((self.root / "invalid").exists())


if __name__ == "__main__":
    unittest.main()
