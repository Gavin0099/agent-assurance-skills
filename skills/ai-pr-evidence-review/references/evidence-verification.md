# Verification evidence

For a GitHub PR, compare independent metadata from the PR and the original run, check suite, or check-run record. Useful read-only surfaces include `gh pr view` for current base/head metadata, `gh run view` for workflow details, and the GitHub Checks API for the tested SHA and individual checks. A check rollup is a discovery aid. Use the source run to confirm the tested revision and whether the relevant jobs and tests executed.

When the objects are already local, a committed diff can be inspected without checkout using `git --no-optional-locks diff --no-ext-diff --no-textconv <merge-base-sha> <head-sha> --`. Resolve named revisions first and use validated full commit IDs. If the history or objects are missing, use available provider artifacts or record the limitation.

| Evidence state | Interpretation |
| --- | --- |
| Exact head | Repository and tested commit match the candidate. Record provider, run/attempt or receipt, conclusion, and executed checks. |
| Tested merge | Provider identifies a different tested SHA and establishes the reviewed head and target revisions used in the merge. Keep those three IDs and the merge-check conclusion together. |
| Stale | Evidence covers a previous head or an outdated integration base. Keep the original conclusion attached to its own revision. |
| Unbound | Provenance, tested revision, attempt, or run-to-test linkage is insufficient. A copied green badge, screenshot, author summary, or run title alone is unbound. |
| Missing | No relevant run or receipt was available in the examined sources. |

Record conclusion independently of binding. Convey skips, cancellation, pending jobs, required jobs with no result, and suites with zero relevant tests. If an observed run contradicts a summary, cite both and use the original record for what was executed. One green required check can coexist with missing coverage or another failing check.

For a local receipt, record command, working directory or repo ID, full revision, dirty state when available, exit code, executed test names or counts, and where the log came from. If workspace inputs or provenance are unclear, limit the claim accordingly. Avoid publishing private logs or identifiers when a redacted excerpt gives the reader the same evidence.
