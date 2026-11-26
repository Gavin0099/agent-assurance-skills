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

## First import verification

The initial import used Framework `c8decc4475f1724bb3fe10bbda8b4ee3e66bf79a` (1.3.0 candidate) at consumer commit `e05384290227fb55121a589400f988d89f3180f5`.

| Check | Observed result |
| --- | --- |
| Contract and baseline | Readiness `ready=true`, drift `severity=ok`, consumer manifest `compatible`. |
| Framework binding | The committed clean lock, submodule gitlink, and checkout SHA matched. |
| Local Git | Pre-commit ran during onboarding. A push to a disposable local bare repo exercised the inventory guard and Framework runtime smoke. |
| Consumer runtime | Quickstart, SessionStart, and PreTask passed. A separate controlled PostTask replay executed the skill package validator successfully. The high-risk fixture emitted an assumption-evidence advisory. |
| Package boundary | The domain validator passed with both complete skill packages and rejected an isolated copy with a missing report template. The installer discovered the same two skills with the Framework initialized. |
| Native agents | Codex SessionStart and Stop were installed and pending trust at import. Claude Code and Copilot configuration checks passed. Live native closeout remains to be verified. |

The pre-commit update advisory saw a staged lock during the first import. The committed lock passed the binding check. The GitHub Actions workflow is configured for future hosted runs.
