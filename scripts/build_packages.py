"""Build deterministic, offline distribution packages from the Community skills."""

import argparse
import hashlib
import json
import re
from pathlib import Path
from zipfile import ZipFile, ZipInfo


ROOT = Path(__file__).resolve().parents[1]
SKILLS = {
    "ai-pr-evidence-review": (
        "SKILL.md", "assets/review-report.md", "references/evidence-verification.md"
    ),
    "agent-acceptance-test": (
        "SKILL.md", "assets/acceptance-report.md", "references/test-design.md"
    ),
}
PORTABLE_SCHEMA = "https://agent-plugins.org/schemas/1.0.0/plugin.schema.json"
ZIP_FILE_MODE = 0o100644 << 16


def repository_file(relative_path: str) -> bytes:
    path = ROOT / relative_path
    if path.resolve(strict=True) != path or not path.is_file():
        raise ValueError(f"Expected a regular repository file: {relative_path}")
    return path.read_bytes().replace(b"\r\n", b"\n")


def json_source(path: str) -> dict:
    return json.loads(repository_file(f"packaging/{path}"))


def json_bytes(value: dict) -> bytes:
    return (json.dumps(value, ensure_ascii=False, indent=2) + "\n").encode("utf-8")


def skill_files(name: str, paths: tuple[str, ...]) -> dict[str, bytes]:
    files = {path: repository_file(f"skills/{name}/{path}") for path in paths}
    text = files["SKILL.md"].decode("utf-8")
    opening, marker, tail = text.partition("---\n")
    frontmatter, closing, _ = tail.partition("\n---\n")
    if opening or not marker or not closing:
        raise ValueError(f"{name} needs SKILL.md frontmatter")
    if not re.search(rf"^name: {re.escape(name)}$", frontmatter, re.MULTILINE):
        raise ValueError(f"{name} needs a matching name")
    if not re.search(r"^description: +\S", frontmatter, re.MULTILINE):
        raise ValueError(f"{name} needs a description")
    for target in re.findall(r"\[[^\[\]\n]+\]\(([^)\s]+)\)", text):
        if target.startswith(("#", "https://", "http://")):
            continue
        if target.partition("#")[0].removeprefix("./") not in files:
            raise ValueError(f"{name} has an unpackaged or external resource: {target}")
    return files


def package_members() -> dict[str, dict[str, bytes]]:
    license_files = {"LICENSE": repository_file("LICENSE")}
    common = json_source("metadata.json")
    interface = json_source("openai/interface.json")
    icon = {"assets/icon.svg": repository_file("packaging/assets/icon.svg")}
    name = common["name"]
    if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name) or len(name) > 64:
        raise ValueError("Plugin name must be lowercase kebab-case, up to 64 characters")
    if not re.fullmatch(r"(0|[1-9]\d*)\.(0|[1-9]\d*)\.(0|[1-9]\d*)", common["version"]):
        raise ValueError("Package version must be a stable MAJOR.MINOR.PATCH version")
    for field, limit in {
        "displayName": 30, "shortDescription": 30, "longDescription": 4000, "developerName": 80
    }.items():
        if not 0 < len(interface[field].strip()) <= limit:
            raise ValueError(f"Invalid listing field: {field}")
    for field in ("logo", "composerIcon"):
        if interface[field] != "./assets/icon.svg":
            raise ValueError(f"{field} must reference the bundled icon")
    packages = {}
    bundle = dict(license_files)
    for skill, paths in SKILLS.items():
        files = skill_files(skill, paths) | license_files
        packages[f"{skill}.zip"] = {
            f"{skill}/{path}": data for path, data in files.items()
        }
        bundle.update({f"skills/{skill}/{path}": data for path, data in files.items()})

    def archive(directory: str, files: dict[str, bytes]) -> dict[str, bytes]:
        return {f"{directory}/{path}": data for path, data in files.items()}

    readme = {"README.md": repository_file("packaging/README.md")}
    packages["agent-assurance-community.zip"] = archive(
        "agent-assurance-community", bundle | readme
    )
    plugin = bundle | readme | icon
    packages["agent-assurance-codex.zip"] = archive(name, plugin | {
        ".codex-plugin/plugin.json": json_bytes(common | {
            "skills": "./skills/",
            "interface": interface,
        })
    })
    packages["agent-assurance-claude.zip"] = archive(name, bundle | readme | {
        ".claude-plugin/plugin.json": json_bytes(common | {
            "displayName": interface["displayName"],
        })
    })
    packages["agent-assurance-cursor.zip"] = archive(name, plugin | {
        ".cursor-plugin/plugin.json": json_bytes(common | json_source("cursor/metadata.json"))
    })
    packages["agent-assurance-openai.zip"] = archive(name, plugin | {
        "plugin.json": json_bytes({"$schema": PORTABLE_SCHEMA} | common | {
            "extensions": {"com.openai": {"interface": interface}},
        })
    })
    return packages


def build(output: Path) -> None:
    packages = package_members()
    output.mkdir(parents=True)
    written = []
    try:
        checksums = []
        for filename, members in sorted(packages.items()):
            path = output / filename
            with path.open("xb") as stream, ZipFile(stream, "w") as archive:
                written.append(path)
                for member, data in sorted(members.items()):
                    # ZipInfo defaults to 1980-01-01 and ZIP_STORED.
                    info = ZipInfo(member)
                    info.create_system = 3
                    info.external_attr = ZIP_FILE_MODE
                    archive.writestr(info, data)
            checksums.append(f"{hashlib.sha256(path.read_bytes()).hexdigest()}  {filename}")

        notes = repository_file("packaging/RELEASE_NOTES.md")
        checksums.append(f"{hashlib.sha256(notes).hexdigest()}  Release Notes.md")
        for filename, data in (
            ("Release Notes.md", notes),
            ("SHA256SUMS", ("\n".join(checksums) + "\n").encode("ascii")),
        ):
            path = output / filename
            with path.open("xb") as stream:
                written.append(path)
                stream.write(data)
    except BaseException:
        for path in written:
            path.unlink()
        output.rmdir()
        raise


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", type=Path, required=True, help="new output directory")
    args = parser.parse_args()
    try:
        build(args.output)
    except (OSError, ValueError) as error:
        parser.exit(1, f"Build failed: {error}\n")
    print(f"Built Community and platform candidates in {args.output}")


if __name__ == "__main__":
    main()
