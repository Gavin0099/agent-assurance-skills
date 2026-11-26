"""Verify that the published Agent Skills carry their local resources."""

import re
from pathlib import Path

from governance_tools.validator_interface import DomainValidator, ValidatorResult


class SkillPackageValidator(DomainValidator):
    @property
    def rule_ids(self) -> list[str]:
        return ["common"]

    def validate(self, payload: dict) -> ValidatorResult:
        packages = Path(__file__).resolve().parents[1] / "skills"
        violations = []
        names = ("ai-pr-evidence-review", "agent-acceptance-test")
        for name in names:
            package = packages / name
            entrypoint = package / "SKILL.md"
            if not entrypoint.is_file() or entrypoint.resolve().parent != package:
                violations.append(f"{name} needs a local SKILL.md")
                continue
            text = entrypoint.read_text(encoding="utf-8")
            for target in re.findall(r"\[[^\[\]\n]+\]\(([^)\s]+)\)", text):
                if target.startswith(("#", "https://", "http://")):
                    continue
                resource = (package / target.partition("#")[0]).resolve()
                if not resource.is_relative_to(package) or not resource.is_file():
                    violations.append(f"{name} has a missing or external resource: {target}")
        return ValidatorResult(
            ok=not violations,
            rule_ids=self.rule_ids,
            violations=violations,
            evidence_summary="Checked both v0.1 skill entrypoints and their relative resource links",
        )


if __name__ == "__main__":
    result = SkillPackageValidator().validate({})
    print(result.evidence_summary)
    for violation in result.violations:
        print(violation)
    raise SystemExit(0 if result.ok else 1)
