# PLAN.md
<!-- governance-baseline: overridable -->
<!-- baseline_version: 1.0.0 -->

> **最後更新**: 2026-11-26
> **Owner**: Gavin0099
> **Freshness**: Sprint (7d)
> **Risk tier**: L2

---

## Current Phase

- [ ] v0.1 · Governance onboarding and independent skill validation.

## Active Sprint

- [ ] Finish the Framework onboarding checks for the `agent-assurance` domain.
- [ ] Complete cross-agent evaluation before releasing either skill. [Tracking issue #1](https://github.com/Gavin0099/agent-assurance-skills/issues/1)

## Backlog

- P1 · Evaluate a portable receipt adapter for `agent-evidence-audit`.

## Decision Log

- 2026-11-26 · Owner selected the `agent-assurance` domain and L2 risk tier. The repo consumes a pinned Framework submodule for development governance. Each published skill carries its own instructions, references, and report template.

## Known Risks

- Claude Code OAuth blocked behavioral validation in the initial v0.1 trials. [Evaluation record](tests/evaluations/initial-results.md)
