"""Check built archives and checksums against the current packaging sources."""

import argparse
import hashlib
from pathlib import Path
from zipfile import BadZipFile, ZipFile

from build_packages import ZIP_FILE_MODE, package_members, repository_file


def validate(output: Path) -> None:
    packages = package_members()
    artifacts = set(packages) | {"Release Notes.md", "SHA256SUMS"}
    if {path.name for path in output.iterdir()} != artifacts:
        raise ValueError("Output must contain exactly the expected archives, notes, and checksums")
    for name in artifacts:
        path = output / name
        if path.is_symlink() or not path.is_file():
            raise ValueError(f"Expected a regular output file: {name}")

    checksums = []
    for name, members in sorted(packages.items()):
        path = output / name
        with ZipFile(path) as archive:
            if archive.namelist() != sorted(members):
                raise ValueError(f"{name} has unexpected, missing, or duplicate entries")
            for member, data in members.items():
                info = archive.getinfo(member)
                if info.create_system != 3 or info.external_attr != ZIP_FILE_MODE:
                    raise ValueError(f"{name} has an unexpected file mode: {member}")
                with archive.open(member) as stream:
                    if stream.read(len(data) + 1) != data:
                        raise ValueError(f"{name} payload differs from source: {member}")
        checksums.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {name}")

    notes = (output / "Release Notes.md").read_bytes()
    if notes != repository_file("packaging/RELEASE_NOTES.md"):
        raise ValueError("Release notes differ from source")
    checksums.append(f"{hashlib.sha256(notes).hexdigest()}  Release Notes.md")
    if (output / "SHA256SUMS").read_bytes() != ("\n".join(checksums) + "\n").encode("ascii"):
        raise ValueError("SHA256SUMS does not match the artifacts")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path)
    args = parser.parse_args()
    try:
        validate(args.output)
    except (BadZipFile, OSError, ValueError) as error:
        parser.exit(1, f"Validation failed: {error}\n")
    print("Validated package members, source contents, release notes and SHA-256 digests")


if __name__ == "__main__":
    main()
