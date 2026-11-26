# Agent acceptance test design

| Area | Stimulus and oracle |
| --- | --- |
| Tool call | Exercise a successful call and a failure or malformed response. Compare tool name, arguments, call count, and observed state to the contract. Check that the agent surfaces unresolved failures. |
| Retry | Simulate transient failure before a write and, where relevant, a lost acknowledgment after a write. Correlate attempts with the same operation and independently count durable effects. Verify any required retry limit. |
| Memory | Start a new session for the same permitted identity and read back the expected state without supplying that state in the test prompt. Where identity isolation is specified, also check a distinct identity. |
| Recovery | Interrupt at a known point, resume through the intended entrypoint, and compare the recovered state and effects with the source of truth. Verify which steps completed before interruption. |
| Task completion | Compare the claim with the expected persisted output, external resource state, or other direct observation. Confirm any promised constraints on quantity, contents, destination, or ownership. |

A useful evidence record includes the case ID, timestamp or run ID, build and environment, input and expected result, observed output and state, and a trace or artifact reference. Keep stable operation and session IDs for retry and recovery tests. Collect only the information needed to check the behavior. Preserve evidence links and redact credentials or personal data in shared reports.

Summarize counts by result and identify each required case that failed, is blocked, or remains unrun. If no case ran, state that explicitly. If every required case passed, scope the conclusion to those cases, inputs, and the tested build and environment.
