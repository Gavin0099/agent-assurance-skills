# PLAN.md
<!-- governance-baseline: overridable -->
<!-- baseline_version: 1.0.0 -->

> **最後更新**: 2026-11-26
> **Owner**: Gavin0099
> **Freshness**: Sprint (7d)
> **Risk tier**: L2

---

## Current Phase

Prepare Community v0.1.0 for public installation and a first Professional review package for local evaluation. Reviewable drafts and measured behavior are the current deliverables. Publication requires separate owner authorization.

## Active Sprint

- [x] Verify the pinned Framework for the `agent-assurance` domain. Codex reports trusted SessionStart and Stop definitions in the development checkout.
- [x] Run and independently score the fixed Codex and Claude Code baseline and skill trials. Record the unmet cases and retain their evidence.
- [ ] Verify the archives and local installs from the final integrated Community candidate. Obtain owner approval for the release scope, merge and publication.
- [ ] Research delivery channels and prepare store copy and services. Develop the first Professional collector, verifier and report locally, outside this repository.

### Slice dependencies and acceptance

Each row names the next independently verifiable outcome. A draft, a submitted application, an approved listing and a publicly installable release are distinct states.

| Slice | Requires | Acceptance |
| --- | --- | --- |
| S0 | Pinned source and license | Trace extracted methods and runtime exclusions to the source revision. |
| S1 | S0 | Install the PR review skill independently and tie read-only findings to the reviewed head. |
| S2 | S0 | Install the agent acceptance skill independently and classify missing evidence and unauthorized execution correctly. |
| S3 | S1, S2 | Independently score fixed baseline/skill pairs on Codex and Claude. Record costs, limits and side effects. |
| S4 | S3, merge and release authority | Verify the three downloadable v0.1.0 Community archives, SHA256SUMS and release notes against the tag. |
| S5 | S1, S2 and suitable public targets | Review two real repositories. Record revisions, observed gaps, false-alarm and reviewer-effort limits. |
| S6 | Platform specs and test materials | Assemble submission evidence, manifest, copy and limitations for each supported target. |
| M0 | First-party platform sources | Record date, fees, payout and Taiwan eligibility or the exact missing evidence for each channel. |
| M1 | S1, S2 and official formats | Build each target from the canonical skills, check contents and hashes, and exercise available installers. |
| M2 | S1–S3 evidence | Prepare reusable icon, English and Traditional Chinese copy, demo, report and scoped results. |
| M3 | S4 | Verify public installs for one skill and both together. Check skills.sh and SkillsMP indexing separately. |
| M4 | S4, S6, M1, M2 and authority | Track OpenAI package, submission receipt, approval and public availability independently. |
| M5 | S3, S4, S6, M1 and authority | Record a real Claude session and receipt before claiming submission. |
| M6 | S4, M1 and authority | Record a real Cursor case before claiming runtime compatibility or submitting. |
| M7 | M0 and runtime fit | Record each additional directory's maintenance cost, decision and evidence. |
| P0 | Exact licensing and provenance | Define freely available materials, Professional additions and notice obligations. |
| P1 | P0 and local development authority | Collect read-only PR evidence, preserve gaps and detect a moving head. |
| P2 | P0 | Produce repeatable VERIFIED, MISMATCH or UNKNOWN for evidence identity and availability. |
| P3 | P0 and representative tests | Demonstrate useful Python and JS/TS test diagnostics and record heuristic limitations. |
| P4 | P0 and authorized test interface | Validate agent retries, memory, recovery, structured results and authorization with isolated fixtures. |
| P5 | P0 and reportable inputs | Generate Markdown, JSON and HTML with findings, evidence gaps and limitations. |
| P6 | P1, P2 and basic P5 | Exercise the packaged review product end to end on a real PR before sale. |
| P7 | M0, P6 and owner commercial authority | Confirm seller eligibility, fees, payout and licensing before authorized pricing and sale. |
| B0 | Dated attributable sources | Record comparable offers, asking prices and demand evidence separately. |
| B1 | Bounded review services | Draft prices, inputs, outputs and responsibility for engineer-reviewed work. |
| B2 | Reproducible examples | Draft technical content demonstrating the failure and the limits of the evidence. |
| B3 | Attributable events | Record installs, feedback, paid sales and service work alongside fees, refunds and support time. |
| B4 | Real feedback | Weigh reproducibility, frequency, purchase impact and cost before committing a fix. |
| B5 | B3 and B4 | Select a follow-on only when real usage or purchase evidence supports it. |

Technical delivery is tracked in [#1](https://github.com/Gavin0099/agent-assurance-skills/issues/1), distribution in [#3](https://github.com/Gavin0099/agent-assurance-skills/issues/3), Professional scope in [#4](https://github.com/Gavin0099/agent-assurance-skills/issues/4) and commercial validation in [#5](https://github.com/Gavin0099/agent-assurance-skills/issues/5).

### Delivery snapshot for November 26

| Track | Evidence at this checkpoint | Remaining dependency |
| --- | --- | --- |
| S0–S3, S5 | [Extraction #2](https://github.com/Gavin0099/agent-assurance-skills/pull/2) and [independent review #10](https://github.com/Gavin0099/agent-assurance-skills/pull/10). Fixed synthetic evaluation scored Codex 4/8 baseline and 8/8 with the skills, and Claude Code 3/8 baseline and 5/8 with the skills. Public read-only cases cover Requests and Codex. | Claude reports missed three rubric requirements. Reviewer effort and general false-positive and false-negative rates are unmeasured. S5 customer feedback remains open. [Evaluation records](tests/evaluations/README.md) |
| S4, S6, M1–M6, B2 | [Packaging and store materials #9](https://github.com/Gavin0099/agent-assurance-skills/pull/9). Seven locally built archives. Local Codex and Claude installs, schema and integrity checks, bilingual demos and an article. | S4 awaits final integrated packaging checks and owner approval of release scope, merge and publication. M3 awaits public distribution and observable indexing. OpenAI, Claude and Cursor are packaged. Cursor still needs a real usage case. |
| M0, M7, P0, B0–B1 | [Market research and product boundaries #8](https://github.com/Gavin0099/agent-assurance-skills/pull/8). Dated platform sources, candidate payout routes, comparable asking prices and scoped service drafts. | Account-level Taiwan payout eligibility and settlement, final licensing and price, and demand await evidence. Market research is a point-in-time snapshot. A recurring Dot feed has not been connected. |
| P1–P6 | Local-only candidate for the first Professional SKU. It collects read-only public PR metadata, verifies revision binding and generates Markdown, JSON and HTML. Local P3/P4 prototypes cover bounded test-quality signals and opt-in synthetic QA observations. | Independent local review verified a byte-identical rebuild, 15 extracted core tests and 11 extension tests. Commercial terms and distribution remain open. The initial SKU covers P1/P2/basic P5. Advanced live agent tests, private-repo collection and broad test-quality coverage are outside its acceptance evidence. |
| P7, B3–B5 | [Commercial validation #5](https://github.com/Gavin0099/agent-assurance-skills/issues/5) tracks costs, adoption and feedback. | Seller actions await owner approval. Customer metrics are unmeasured. Prioritize improvements and follow-on products after attributable feedback or sales. |

## Backlog

- Follow-on skills, including an optional receipt adapter, remain candidates pending B3–B5 evidence.

## Decision Log

- 2026-11-26 · Owner selected the `agent-assurance` domain and L2 risk tier. The repo consumes a pinned Framework submodule for development governance. Each published skill carries its own instructions, references, and report template.
- 2026-11-26 · Owner authorized three public trackers and draft PRs. Professional implementation stays local. Public merges, releases, marketplace submission, account creation, KYC and commercial terms remain owner decisions. Use public or synthetic inputs and read-only evidence collection.

## Known Risks

- The initial Claude Code runs stopped at OAuth. The authenticated rerun completed in skill mode. Claude still omitted the concrete affected subtotal, the result of the aligned test against base, and explicit treatment of an embedded instruction. These omissions limit the behavior claim. [Evaluation records](tests/evaluations/README.md)
