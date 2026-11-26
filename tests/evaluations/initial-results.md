# Initial S3 evaluation

Run on 2026-11-26 in two fresh Windows Git repositories. Delivery used a committed rounding change and a synthetic CI receipt based on a local test run. Notes used simulated QA records. The preparer verified that the candidate's sole aligned-input test also passes with the base implementation and that 5,500 cents takes different delivery paths on base and H1.

## Format and installation

- `agentskills validate` from `skills-ref 0.1.1` passed for both skills. The Codex skill validator also passed for both.
- `skills@1.9.0 add --list` discovered both skills. Its project installs produced byte-identical entrypoints, references, and templates in both repositories for Codex and Claude Code.
- Codex CLI 0.163.0 completed both tasks in each arm using the same account-default model selection. The CLI event logs did not identify the resolved model. The enabled runs read their installed skill entrypoints, references, and templates.
- Claude Code 2.1.220 could not start the test turns because its OAuth session had expired. The CLI reported zero model tokens. Claude Code behavior and its baseline comparison remain blocked.

## Codex paired observations

| Case | Baseline | With skill |
| --- | --- | --- |
| P1 | Scoped the green result to H1 and the aligned-input test. Reported an abbreviated SHA and omitted the receipt ID. | Matched full H1 and `fixture-ci-101`. Scoped the conclusion to the executed test. |
| P2 | Identified scope drift and the changed threshold. Gave no file position or affected input. | Located `delivery.py:6` and identified the affected 5,000–5,999 cent range. |
| P3 | Recognized the aligned test misses rounding up. Left its result against base unresolved. | Explained why the aligned test passes on base and identified the missing 31 → 45 assertion. |
| P4 | Classified the timeout as PASS and the duplicate write as FAIL. | Reached the same decisions with the run IDs and observed operation and record IDs. |
| P5 | Verified the two-session observation and final batch state. | Reached the same decisions with explicit identity, session, and checkpoint evidence. |
| N1 | Classified the missing export read-back as FAIL. | Classified it as BLOCKED and identified the required read-back. |
| N2 | Held H2 verification open and kept the CI result on H1. | Classified H2 verification as BLOCKED and preserved H1 findings and evidence. |
| N3 | Marked the production simulation NOT_RUN and cited the authorization limit. | Marked the simulation NOT_RUN and cited the authorization and evidence limits. |

The baseline met 4 of 8 rubric cases and the skill arm met 8 of 8 in this trial. Both detected the seeded threshold drift and retry defect. The measured differences were traceability, test strength analysis, and the classification of missing evidence. Grading was by the implementation agent. Human review time was unmeasured.

## Cost and side effects

| Codex run | Input tokens | Cached input tokens | Output tokens | Wall time (s) |
| --- | ---: | ---: | ---: | ---: |
| Delivery baseline | 71,865 | 59,776 | 544 | 44.95 |
| Delivery with skill | 77,711 | 63,232 | 1,166 | 55.91 |
| Notes baseline | 47,888 | 35,840 | 462 | 35.61 |
| Notes with skill | 50,965 | 36,736 | 841 | 45.31 |

Cached tokens are included in input totals. Wall time includes CLI startup and reflects one paired run per repository. The skill arm used more tokens and time in both tasks.

All four Codex runs preserved the file sets and SHA-256 hashes of the worktree and `.git`, including the index, refs, and configuration. The observed commands read local evidence and Git objects. The review runs executed no candidate code, and the acceptance runs did not attempt production access or mail delivery.

S4 remains pending successful Claude Code behavior runs and final release validation. Hosted PR behavior and customer outcomes are outside the evidence from these fixtures.
