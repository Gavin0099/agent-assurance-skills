# S5 public repository validation

One independent AI reviewer applied the [PR evidence review skill](../../skills/ai-pr-evidence-review/SKILL.md) to a Requests testing change and the [agent acceptance skill](../../skills/agent-acceptance-test/SKILL.md) to a Codex TUI recovery change. Both cases use genuine merged PRs from unrelated repositories. Review used public GitHub API reads for PR requirements, changed files, commit comparisons, CI jobs and available logs. Target code was neither installed nor run. The review created no state in either target repository. This exercise covers the skills' evidence-review workflows. It does not measure fresh-agent install or activation, independent human agreement, or runtime performance.

## Requests — test environment isolation

| Review input | Observed value |
| --- | --- |
| Reviewed PR | [psf/requests #7423](https://github.com/psf/requests/pull/7423) |
| Target tip supplied by PR and comparison merge base | `e8d2c015eecda8273612dd4562425e00cd164ba5` |
| Candidate head | `da905d0eb1de1184d323d39dfc2ce2b423df7bee` |
| Recorded merge commit | `25340ebad09a38e0748aeb26232102022a03ec94` |
| Snapshot | GitHub PR and CI checked on 2026-11-26 between 15:02 and 15:05 UTC. PR base and head were unchanged at recheck. |

The PR description calls for removing inherited proxy settings from tests. The pinned comparison adds a single function-scoped autouse fixture. It unsets lower- and uppercase HTTP, HTTPS, FTP, no-proxy and all-proxy environment keys through pytest's monkeypatch fixture. The base lacked this suite-wide fixture. Static review supports the intended isolation change for the listed keys and found no unrelated product change in the single-file diff. [PR files](https://github.com/psf/requests/pull/7423/files) · [Fixture on the reviewed head](https://github.com/psf/requests/blob/da905d0eb1de1184d323d39dfc2ce2b423df7bee/tests/conftest.py#L25-L31)

**Coverage gap at `tests/conftest.py:26`.** The change adds no dedicated assertion or evidence from a pre-seeded process environment. A suite run with the listed variables already absent could stay green on the base and on the candidate. This is a limitation of the recorded verification, with no established behavioral defect. A separately authorized test with an inherited sentinel could verify the keys are absent inside test scope and restored outside it. [Candidate fixture](https://github.com/psf/requests/blob/da905d0eb1de1184d323d39dfc2ce2b423df7bee/tests/conftest.py#L25-L31)

**Verification decision.** GitHub associates the successful Python 3.13 / Ubuntu 22.04 job with candidate head `da905d0…`, completed 2026-05-10 at 21:26:35 UTC. The PR workflow config runs `make ci` and uses an implicit checkout ref. The job logs returned HTTP 410, leaving the exact checked-out commit, case list and starting environment unverified. The successful workflow is recorded at its provider-reported scope. Direct execution evidence for the isolation requirement is **BLOCKED**. The later merge commit has its own identity and cannot substitute for the candidate receipt. [Job record](https://github.com/psf/requests/actions/runs/25640181937/job/75259156282) · [Workflow on candidate head](https://github.com/psf/requests/blob/da905d0eb1de1184d323d39dfc2ce2b423df7bee/.github/workflows/run-tests.yml)

## Codex TUI — automatic recovery of disconnected conversations

| Acceptance input | Observed value |
| --- | --- |
| Specification | [openai/codex #63211](https://github.com/openai/codex/pull/63211) |
| Target tip supplied by PR and comparison merge base | `4ae20b9f28f72d46fcea7431381b88fb4c70514a` |
| Candidate head and recorded merge commit | `44848822b1a58fa40cdcd89ec3161c757735cfd0` |
| Environment, entrypoint and effects | Rust TUI recovery after cloud stream disconnect. Public Windows Bazel CI and source for simulated app-server tests. Review authorization was limited to reading public metadata, code and logs. |
| Snapshot | GitHub PR and CI checked on 2026-11-26 between 15:02 and 15:05 UTC. PR base and head were unchanged at recheck. |

The PR says quiet recovery should preserve draft and queued input, resume when paginated history is verifiable, and stay paused with an error when it is incomplete. The oracle is the reconstructed chat state, stream state, rendered error, and count of user-turn submissions after a controlled response. The test drives the real TUI state machine with an in-process cloud-client command channel and synthetic replies. Production network behavior and durable data in a hosted conversation fall outside that simulation. [Recovery entrypoint](https://github.com/openai/codex/blob/44848822b1a58fa40cdcd89ec3161c757735cfd0/codex-rs/tui/src/app/resume_preparation.rs#L89-L117) · [Regression test](https://github.com/openai/codex/blob/44848822b1a58fa40cdcd89ec3161c757735cfd0/codex-rs/tui/src/app/tests/session_lifecycle_requests.rs#L261-L531)

| Case | Stimulus and expected observation | Public evidence and decision |
| --- | --- | --- |
| Draft and queue | Interrupt an idle cloud stream with a draft and queued message. During recovery keep input and suppress outbound user turns. On validated recovery submit the queued turn exactly once. | The test asserts draft text, the queued message and submission count. **BLOCKED** for named-case verification because the observed CI log reports the test target only. |
| Delayed or newly available history | Return delayed history or a newly persisted turn through the simulated channel. Retry the incomplete read, install the recovered session and read back the expected history. | The test asserts the delayed sequence of reads and the final store contains the new turn in the changed-history case. **BLOCKED** for named-case verification. |
| Unverifiable history | Return repeated cursors, persistently empty pages or a scan-limit condition. Keep sending paused, retain the draft and render an error. | The test checks bounded reads, disconnected state, zero submissions and visible error. **BLOCKED** for named-case verification. |
| Navigation during recovery | Switch the displayed conversation during a pending recovery handoff. Keep the new selection and suppress a submission to the old thread. | The test checks both displayed thread IDs and the submission count. **BLOCKED** for named-case verification. |
| Live service | Verify recovery and durable state across an actual cloud disconnect. | **NOT_RUN** in this review. It was intentionally limited to public evidence with no live credentials or writes. |

At `resume_preparation.rs:103` and `:106`, the candidate guards against active or pending user turns and outstanding question-answer history. The reviewed regression test starts with an idle thread and does not directly exercise both exclusions. Their implementation is visible statically. Additional case-level evidence is needed before crediting them as verified. [Guard code](https://github.com/openai/codex/blob/44848822b1a58fa40cdcd89ec3161c757735cfd0/codex-rs/tui/src/app/resume_preparation.rs#L103-L108)

**What ran.** GitHub Actions run `45082305996`, attempt 1, reports overall failure. The Windows shard 3/4 job `137392965515`, completed 2026-11-22 at 23:52:54 UTC, reports the full reviewed SHA in its checkout log. That log records `//codex-rs/tui:tui-unit-tests` as passing in 66.7 seconds. The build definition includes the source file containing the recovery test. The inspected log does not enumerate that test by name. The same job records a V8 build failure caused by insufficient disk space. Thus the TUI target pass and the failed job both stand at their own scope. The available records do not establish a failed recovery case or an overall pass. A PR bot's review comment identifies a different commit and cannot validate the current head. [Windows shard](https://github.com/openai/codex/actions/runs/45082305996/job/137392965515) · [Bazel test target](https://github.com/openai/codex/blob/44848822b1a58fa40cdcd89ec3161c757735cfd0/codex-rs/tui/BUILD.bazel) · [PR review comment](https://github.com/openai/codex/pull/63211#issuecomment-7087423765)

## Outcome and measurement gaps

Two scoped public-evidence reviews completed. Each surfaced a concrete evidence gap. A green Requests workflow can create a false positive if treated as direct verification of inherited-variable isolation. A red Codex aggregate can create a false negative if treated as a failed recovery case without checking the checkout, target result and infrastructure error. These are examples of misinterpretation avoided during this review. Actual false-positive and false-negative counts remain unknown without independent defect ground truth. Human review time was unmeasured. Neither case establishes general effectiveness, and these reviews add no Claude evidence or release authorization.
