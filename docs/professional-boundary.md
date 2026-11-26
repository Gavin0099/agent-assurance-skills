# Community and Professional product boundary

2026-11-26 · P0 · Product and distribution design

| Capability | Community v0.1 candidate | Professional scope |
| --- | --- | --- |
| PR evidence review | Standalone workflow, basic report, manual check of revision, CI and test evidence | Same workflow supported by automated collection and verification |
| Agent acceptance | Standalone case design, evidence capture and basic report | Reusable fixtures, adapters and expanded scenario coverage in P4 |
| GitHub PR evidence | Reviewer-provided or manually collected facts | P1 read-only snapshot including exact base and head, changed files, checks and reviews |
| Revision and receipt validation | Manual assessment of scope and evidence | P2 deterministic revision binding, stale CI detection and explicit missing evidence |
| Test quality | Manual analysis against requirements | P3 assisted inspection and scoped test comparisons with approval |
| Report | Basic Markdown templates | P5 Markdown, JSON and HTML renders with evidence provenance and limitations |
| Batch PR review | Individual workflow | Candidate after evidence of demand |

P6's first product requires P1, P2 and a basic P5 report, validated against the same revision. Charge for automation, repeatability, support and delivery. A verified revision binding establishes the provenance of evidence. Human review assesses requirements and behavioral correctness.

## Source and distribution

- The two public skills declare Apache-2.0 and ship from the product repository under its root license. The reviewed source is the [PR #2 head](https://github.com/Gavin0099/agent-assurance-skills/tree/fd03071209b2a6ebdab60a5c4e2dbd70cba0a43c). The [source inventory](public-extraction-validation.md#s0--source-inventory) maps the standalone instructions to Framework concepts. The original extraction rewrote the flows and uses ordinary logs and run metadata.
- The Framework gitlink and inventory identify [c8decc4475f1724bb3fe10bbda8b4ee3e66bf79a](https://github.com/Gavin0099/ai-governance-framework/tree/c8decc4475f1724bb3fe10bbda8b4ee3e66bf79a). Its [exact-revision LICENSE](https://raw.githubusercontent.com/Gavin0099/ai-governance-framework/c8decc4475f1724bb3fe10bbda8b4ee3e66bf79a/LICENSE) is Apache-2.0. The complete pinned Git tree and product candidate tree each contained a root LICENSE and no NOTICE file at inspection.
- Standalone P1, P2 and P5 candidates can use their own implementation and ordinary provider APIs while the commercial license is undecided. Work added to this public product repository should follow its Apache-2.0 license. A separately owned Professional implementation intended for proprietary distribution requires the owner's decision about repository and terms before exposure. `Gavin0099/agent-assurance-pro` is a proposed location.
- If distributing copied or modified Apache-2.0 material, include the license in each package containing it, retain applicable upstream notices in distributed source, mark modified files and carry applicable attribution from any upstream NOTICE found at the actual selected revision. Record the source repository, commit, paths, license and modifications for any reused component and verify direct dependencies separately. Commercial terms for additional work must preserve Apache-2.0 rights for covered material. Review platform terms against those rights before including Community files. [Apache License 2.0, sections 4–6](https://www.apache.org/licenses/LICENSE-2.0)

A package whose copied source, permissions or attribution cannot be traced stays out of distribution until the missing evidence is resolved. Keep executable dependencies and Framework runtime out of the candidate when ordinary API data and standalone checks suffice. Any customer repository access must be scoped to the authorized review or test.
