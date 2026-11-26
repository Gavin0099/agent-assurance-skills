# Evaluate skills on two fresh repositories

These fixtures model an AI-written code change and an agent acceptance request. Both project repositories contain only synthetic material and use ordinary Git without Framework configuration. The [task prompts and grading rubric](cases.md) define five positive and three negative scenarios.

See the [initial S3 results](initial-results.md) for the installation and trial observations and the [independent review](independent-review.md) for the rescored Codex cases, resource measurements, and evidence limits.

## Prepare the inputs

1. Create a temporary `delivery` Git repo outside this project. Commit the contents of [base](../fixtures/delivery/base) and [the ticket](../fixtures/delivery/ticket.md). Record the full base SHA.
2. Overwrite the code with [candidate files](../fixtures/delivery/candidate) and commit the result as H1. At H1 run `python -B -m unittest discover -v` as the fixture preparer. The aligned-input test should pass. Record the command, output and status.
3. Restore the threshold in `delivery.py` to 5,000 cents and commit H2. Put the observed values into `review-input.json` at the root of the fixture. Use the full revisions in `base_sha`, `head_at_start` (H1), and `head_at_report` (H2). Put the H1 test under `ci_runs` with `id`, `repository`, `tested_sha`, `command`, `conclusion`, and `executed_tests`. Label the record as synthetic CI, based on the preparer's local run. Supply zero H2 runs.
4. Create and initialize a second Git repo named `notes`. Commit the [note assistant specification and QA observations](../fixtures/notes). The observations represent a simulator. They are supplied evidence about that simulated environment.
5. Copy each initialized repo into a baseline and skill-enabled project for each agent. Keep the commits and provided data identical. In the skill-enabled projects install the relevant skills from the local source using `npx skills add /path/to/agent-assurance-skills --skill ai-pr-evidence-review --skill agent-acceptance-test -a codex -a claude-code --copy --yes`. Install outside any customer workspace. Record the exact CLI versions and check that the entrypoint, references, and templates are present.

## Run and compare

- In new Codex and Claude Code sessions, run the identical task prompt in [cases.md](cases.md) without a skill in baseline projects and with the corresponding skill activated in enabled projects. Record installation and activation as separate observations. Keep model, authorization, fixture content, tools, and runtime settings comparable. Record meaningful differences if the agent does not expose a setting or metric.
- Keep logs and reports outside the two repos. Capture the pre/post repository state after installation and compare it with the boundary rules in the rubric. Inspect agent traces for unauthorized execution or hosted actions. Record each rubric outcome, unsupported findings, observed side effects, token counts when available, elapsed seconds, and grader review time. Mask arm labels when practical. Report missing measurements explicitly.
- Compare per-case decisions before and after skill activation. Report the raw outcome and scope. Human review time requires an actual human grader. External PR compatibility, savings, and comparative effectiveness need data beyond these seeded cases.
