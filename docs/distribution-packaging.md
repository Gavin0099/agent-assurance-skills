# Community distribution candidates

Generate seven ZIPs, release notes, and SHA-256 digests with Python 3.10 or newer. The build is offline and uses `skills/` as the source for all variants. Markdown, JSON, SVG, and the Apache 2.0 license are the only payloads. The input list explicitly includes each distributed skill and its resources. If you add a resource, include it in that list and link to it from the skill.

```sh
python -B scripts/build_packages.py --output dist-candidate
python -B scripts/validate_packages.py dist-candidate
python -B -m unittest discover -s tests -p test_distribution_packages.py -v
```

Choose a new output directory for each build. Validate it before use. The validator requires the corresponding source revision and compares every archive member with its generated source payload, then verifies the notes and SHA-256 digests. ZIPs use fixed timestamps, file modes and ordering. The builder normalizes CRLF to LF in the text payloads. An incomplete build cannot pass validation.

## Install and validate locally

| Target | Candidate and steps |
| --- | --- |
| Single skills and Community | Extract either single-skill ZIP or `agent-assurance-community.zip`, and pass the extracted folder to `npx skills@1.9.0 add <folder> --list`. To install, replace `--list` with `--skill <name> -a codex -a claude-code --copy --yes`. Use `ai-pr-evidence-review` for the PR review ZIP, `agent-acceptance-test` for the agent acceptance ZIP, or both `--skill` arguments for the bundle. Each ZIP includes the Apache 2.0 license and per-skill references and templates. |
| Codex | Extract `agent-assurance-codex.zip` into a local catalog root, and copy `packaging/codex/marketplace.json` to `<catalog>/.agents/plugins/marketplace.json`. Run `codex plugin marketplace add <catalog>` and `codex plugin add agent-assurance@agent-assurance-local`, preferably with an isolated `CODEX_HOME`. |
| Claude Code | Extract `agent-assurance-claude.zip` into a local catalog root, and copy `packaging/claude/marketplace.json` to `<catalog>/.claude-plugin/marketplace.json`. Run `claude plugin validate <catalog>/agent-assurance --strict` and `claude plugin validate <catalog> --strict`. For an isolated install, set `CLAUDE_CONFIG_DIR` to a test directory, run `claude plugin marketplace add <catalog>` and `claude plugin install agent-assurance@agent-assurance-local`, then check `claude plugin list --json`. |
| Cursor | Extract `agent-assurance-cursor.zip`. For a local test, place the extracted `agent-assurance` directory under `~/.cursor/plugins/local/`, reload Cursor, and confirm both skills appear in Customize. Run the PR example from the [evaluation cases](../tests/evaluations/cases.md) and record the result before claiming runtime compatibility. |
| OpenAI Plugins Directory | `agent-assurance-openai.zip` is a skills-only package with a portable `plugin.json`, OpenAI listing metadata, and both icon paths. The developer portal uses a verified developer identity and applies its own scans and review. |

On Windows with a redirected app directory, resolve the absolute filesystem paths of the catalog, source, configuration, and install working directory before invoking the host CLIs. In the validation environment some commands reported cross-device rename failures on the redirected paths and worked with the canonical paths.

## Readiness as checked on 2026-11-26

| Channel | Evidence and remaining condition |
| --- | --- |
| GitHub and skill registries | Local single-skill and bundle copies into both Codex and Claude Code project destinations work with `skills@1.9.0`. The public default branch at `0abeff7602bdd5d4a9dd6207f66cf5ac96d894e4` returned `SKILLS_NO_VALID_SKILLS` under `--list`. Public release and registry indexing are pending. Recheck after the approved skills revision reaches the public default branch. [skills.sh CLI](https://www.skills.sh/docs/cli) |
| Codex | Local catalog discovery and native plugin install verified on Codex CLI 0.163.0. Model behavior on this exact package was not exercised. [OpenAI packaging docs](https://developers.openai.com/plugins/build/plugins) |
| Claude | Both manifests passed strict validation, and Claude Code 2.1.220 installed the candidate in an isolated local configuration. Behavioral evaluation on the installed plugin remains pending. Anthropic's directory requires a qualifying paid account and a GitHub repository/path the portal can validate. Anthropic's separate official Claude Code marketplace uses a different listing route. [Claude Code distribution](https://code.claude.com/docs/en/plugins/publish) · [Directory checklist](https://claude.com/docs/plugins/pre-submission-checklist) |
| Cursor | Archive content and layout checked against the documented format. Cursor was unavailable in the test environment, so a real local run remains pending. The Cursor Marketplace reviews a public Git repository containing the generated plugin files. [Local testing](https://cursor.com/docs/plugins) · [Cursor submission checklist](https://cursor.com/docs/reference/plugins) |
| OpenAI | `PACKAGED`. The portable manifest passed the published Agent Plugins JSON Schema. The OpenAI extension was checked against documentation locally. Portal validation, submission, approval and publication remain unverified. The five-positive and three-negative MCP review requirement applies to initial MCP app reviews. [Submission docs](https://developers.openai.com/plugins/deploy/submission) · [Portable manifest schema](https://agent-plugins.org/schemas/1.0.0/plugin.schema.json) |

The [fixture cases](../tests/evaluations/cases.md) and [sample report](../examples/sample-review-report.md) provide repeatable examples for reviewers. The plugin ships no executable, installation hook, MCP endpoint, or bundled credentials. The PR evidence workflow reads the surfaces the user makes available. Any acceptance case that performs an operation requires the user's authorization for the interface and its effects.
