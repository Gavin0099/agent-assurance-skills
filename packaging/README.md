# AI Agent Assurance

Review AI-generated code and evaluate agent behavior with reproducible evidence.

- **AI PR Evidence Review** compares a ticket with the candidate changes, inspects test quality, and ties CI results to the reviewed commit. It preserves repository and PR state.
- **Agent Acceptance Test** designs cases and evaluates available evidence. Execution requires a separately authorized test interface and defined side effects.

In your agent, ask to use `ai-pr-evidence-review` with the requirements and PR evidence, or `agent-acceptance-test` with the specification and traces. Claude Code plugin users can invoke `/agent-assurance:ai-pr-evidence-review` or `/agent-assurance:agent-acceptance-test`. Both skills can review supplied evidence without an MCP server.

See the [source and installation guide](https://github.com/Gavin0099/agent-assurance-skills) for sample cases. The license is Apache 2.0.
