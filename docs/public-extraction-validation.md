# Agent Assurance Skills — Public Extraction & Validation

The v0.1 scope is read-only PR evidence review and agent acceptance testing. The standalone skills can be evaluated independently of the Framework's Gate 3 and Gate 4.

[GitHub tracking issue #1](https://github.com/Gavin0099/agent-assurance-skills/issues/1)

## S0 — Source inventory

Source snapshot [ai-governance-framework@c8decc44](https://github.com/Gavin0099/ai-governance-framework/tree/c8decc4475f1724bb3fe10bbda8b4ee3e66bf79a) contains 11 `.agents/skills` and 9 `.claude/skills` entrypoints.

| Source surface | Portable behavior | Extraction decision |
| --- | --- | --- |
| `reviewer-handoff`, `pr-review-merge-gate` | Compare actual scope, preserve disagreements, tie review and integration evidence to the candidate and base | Rewrite as review instructions. The handoff tools, owner merge predicates, and publication artifacts stay in the Framework. |
| `precommit`, `runtime-smoke` | Match validation to the changed scope and distinguish setup failures, execution failures, and gaps | Rewrite as test-quality review and case-level acceptance. The wrappers, dispatcher, and runtime validators stay in the Framework. |
| `test_evidence_receipt_writer.py`, `claim_enforcement_receipt_validator.py` | Identify the executed command, revision, outcome, and supporting evidence of a claim | Use ordinary logs and run metadata in v0.1. A future `agent-evidence-audit` can add an optional Framework receipt adapter. |
| `wrap-up`, hooks, memory, R1/R2 | Show that a completion claim needs independent evidence | Keep lifecycle enforcement and identity ownership in the Framework. |
| `external-onboarding`, `external_repo_readiness.py` | Assess readiness for Framework adoption | Defer `governance-readiness`. Its existing implementation depends on Framework contracts, tooling, and hook state. |
| `codex-review-fast`, qualification artifacts | Historical infrastructure and outcome records | The review skill is a deprecated redirect. Defer `coding-agent-benchmark` pending a reproducible protocol, production binding, and paired runs. |

## S1–S6 — Delivery and exit criteria

| Slice | Deliverable | Exit criteria |
| --- | --- | --- |
| S1 | `ai-pr-evidence-review` | Install independently and produce an evidence-backed report covering scope, code risk, test quality, and candidate-head evidence. Preserve source and repository state. |
| S2 | `agent-acceptance-test` | Install independently and show explicit PASS, FAIL, BLOCKED, and NOT_RUN outcomes against observable oracles. Record authorized execution and supplied evidence distinctly. |
| S3 | Fixtures and paired evaluation | Run at least five positive and three negative cases across at least two repositories without Framework components. Exercise Codex and Claude Code. Compare the same tasks with and without the skills under the same conditions. Record detection, false positives, repository effects, token use, wall time, and manual review time where measurable. |
| S4 | GitHub v0.1.0 and skills.sh | Pass format, cross-agent installation and behavior, and release safety checks. Verify discovery from the public source and create the versioned release. skills.sh visibility depends on its index. |
| S5 | External feedback | Use consented Upwork-style cases to measure reviewer effort and error detection. Track validation evidence and user feedback before making any effectiveness or cost claims. |
| S6 | OpenAI Plugins Directory | Prepare a skills-only package and listing after release validation. Complete required scans, verified developer identity, and portal submission and review. |

The five positive and three negative cases are project acceptance criteria. OpenAI currently applies the specified MCP app review case counts to initial MCP app reviews. [OpenAI submission documentation](https://developers.openai.com/plugins/deploy/submission)

Release validation should include an inspection of package contents for unexpected executables, network behavior, sensitive data, and untrusted instructions. Check that the review skill writes no source or Git state, and that the acceptance skill does not execute cases outside the user's permitted interface and effects. Use the [evaluation procedure](../tests/evaluations/README.md) to record results. A single run establishes only what was observed in that run.
