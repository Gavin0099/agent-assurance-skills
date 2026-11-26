# Repository governance

This repository uses a pinned AI Governance Framework submodule for development. The owner selected domain `agent-assurance` and risk tier `L2`. Public Agent Skills carry their own package resources and can be installed independently.

## Set up a development checkout

From the repository root, initialize the pinned Framework. Install PyYAML into the Python environment used by Git and the coding agents. The commands below use PowerShell.

```powershell
git submodule update --init --recursive
$repoRoot = (Resolve-Path .).Path
$framework = (Resolve-Path additional/ai-governance-framework).Path
$env:PYTHONPATH = $framework
python -m pip install "pyyaml>=6.0"
python -B -X utf8 -m governance_tools.hook_installer --repo $repoRoot --framework-root $framework
python -B -X utf8 -m governance_tools.manage_agent_closeout --project-root $repoRoot install --agent claude
```

The checkout includes the portable Codex SessionStart and Stop definitions. Review both in Codex's `/hooks` before use. The Claude installer creates local SessionStart and SessionEnd settings. Git and Copilot use the official Framework installer. Re-run the installer after creating a fresh clone so its local Git hooks resolve the pinned Framework.

## Verify

```powershell
python -B -X utf8 -m governance_tools.hook_install_validator --repo $repoRoot --framework-root $framework
python -B -X utf8 -m governance_tools.external_repo_readiness --repo $repoRoot --framework-root $framework
python -B -X utf8 -m governance_tools.external_repo_smoke --repo $repoRoot --contract "$repoRoot/contract.yaml" --risk high
python -B -X utf8 -m governance_tools.governance_drift_checker --repo $repoRoot --framework-root $framework
python -B -X utf8 validators/skill_packages.py
```

Use `PLAN.md` for scope and `contract.yaml` for the domain and validator. For a future Framework update, follow the F-7 path specified in `AGENTS.md` and establish evidence for the updated gitlink.
