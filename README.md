# AI Agent Assurance

Verify AI-generated changes, tests, and completion claims with reproducible evidence.

| Skill | What you give it | What you get |
| --- | --- | --- |
| [AI PR Evidence Review](skills/ai-pr-evidence-review/SKILL.md) | A ticket, PR or committed branch diff, and available CI records | A read-only review covering scope, code risk, test quality, and evidence tied to the reviewed commit |
| [Agent Acceptance Test](skills/agent-acceptance-test/SKILL.md) | An agent specification, available traces, and any authorized test interface | A test matrix and a report with evidence-backed PASS, FAIL, BLOCKED, and NOT_RUN outcomes |

Both skills work without the AI Governance Framework. Reviews preserve target repository and PR state. Agent testing starts with case design and evidence evaluation. Test execution requires an authorized interface and defined side effects.

## Try from a checkout

Run these commands from the project where you want to use the skills. The agent destinations are selected at install time.

```sh
npx skills add /path/to/agent-assurance-skills --list
npx skills add /path/to/agent-assurance-skills --skill ai-pr-evidence-review --skill agent-acceptance-test -a codex -a claude-code --copy --yes
```

Start the agent in that project. Ask it to use the named skill and give it the target, requirements, available evidence, and any authorized output path.

- **PR review** — “Use ai-pr-evidence-review to review PR #42 against ENG-19. Check whether CI was run on the current head. Return the report here.”
- **Agent QA** — “Use agent-acceptance-test to check our note assistant against this specification and supplied traces. Evaluate evidence only.”

See [an example PR report](examples/sample-review-report.md), the [extraction and release plan](docs/public-extraction-validation.md), and the [reproducible evaluation cases](tests/evaluations/README.md).

## License

[Apache 2.0](LICENSE)
