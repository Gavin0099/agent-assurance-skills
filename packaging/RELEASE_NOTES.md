# Community v0.1.0 release candidate

- AI PR Evidence Review covers scope, code risk, test quality, and CI evidence tied to the candidate commit.
- Agent Acceptance Test records observed passes, failures, blockers, and cases left unrun. Test execution requires explicitly authorized interfaces and effects.
- The single-skill and Community ZIPs include skill instructions, local references, report templates, and the Apache 2.0 license. Verify ZIP digests against SHA256SUMS.

Extract the desired versioned ZIP and follow the [project installation guide](https://github.com/Gavin0099/agent-assurance-skills). Use the Community ZIP for both skills or either single-skill ZIP for an individual install. The skills require no AI Governance Framework runtime. Their read-only instructions rely on host permissions and sandbox settings for enforcement.

The fixed rubric covered eight cases across two synthetic repositories. Codex scored 4/8 baseline and 8/8 with the skills. Claude Code scored 3/8 baseline and 5/8 with the skills and missed the affected subtotal, the aligned test's result on base, and explicit treatment of an embedded instruction. These were standalone skill-mode trials. Native Codex and Claude plugin installation was checked separately. [Evaluation records](https://github.com/Gavin0099/agent-assurance-skills/tree/main/tests/evaluations)

Cursor runtime use and the OpenAI developer portal remain unverified. Public GitHub downloads and skill indexes depend on release and subsequent discovery checks.
