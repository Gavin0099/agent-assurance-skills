# AI Agent Assurance

Verify AI-generated changes, tests, and completion claims with reproducible evidence.

| Skill | What you give it | What you get |
| --- | --- | --- |
| [AI PR Evidence Review](skills/ai-pr-evidence-review/SKILL.md) | A ticket, PR or committed branch diff, and available CI records | A read-only review covering scope, code risk, test quality, and evidence tied to the reviewed commit |
| [Agent Acceptance Test](skills/agent-acceptance-test/SKILL.md) | An agent specification, available traces, and any authorized test interface | A test matrix and a report with evidence-backed PASS, FAIL, BLOCKED, and NOT_RUN outcomes |

Both skills work without the AI Governance Framework. The PR review instructions tell the agent to preserve target repository and PR state. Filesystem and tool restrictions are enforced by the host's permissions and sandbox configuration. Agent testing starts with case design and evidence evaluation. Test execution requires an authorized interface and defined side effects.

## Install from a versioned ZIP or a checkout

When a GitHub release is available, download the archive for the desired version and check its SHA-256 digest against that release's `SHA256SUMS`. Extract the Community bundle to install both skills, or extract a single-skill ZIP. From the project where you want to use the skills, substitute the extracted directory or the checkout path in these commands.

```sh
npx skills@1.9.0 add /path/to/extracted-folder-or-checkout --list
npx skills@1.9.0 add /path/to/extracted-folder-or-checkout --skill ai-pr-evidence-review --skill agent-acceptance-test -a codex -a claude-code --copy --yes
```

For a single-skill ZIP, keep only its `--skill` selector. Choose either or both of the supported local agent destinations by retaining their `-a` arguments. See the [package guide](docs/distribution-packaging.md) for native plugin installation.

Start the agent in that project. Ask it to use the named skill and give it the target, requirements, available evidence, and any authorized output path.

- **PR review** — “Use ai-pr-evidence-review to review PR #42 against ENG-19. Check whether CI was run on the current head. Return the report here.”
- **Agent QA** — “Use agent-acceptance-test to check our note assistant against this specification and supplied traces. Evaluate evidence only.”

See [an example PR report](examples/sample-review-report.md), the [extraction and release plan](docs/public-extraction-validation.md), and the [reproducible evaluation cases](tests/evaluations/README.md).

## Evaluation

In two synthetic repositories, the fixed rubric yielded Codex scores of 4/8 baseline and 8/8 with the skills, and Claude Code scores of 3/8 baseline and 5/8 with the skills. These trials exercised installed standalone skills in fresh sessions. Native plugin installs were checked separately. The scores describe traceability, analysis and evidence classification in these fixtures. [Evaluation records](tests/evaluations/README.md)

## License

[Apache 2.0](LICENSE)
