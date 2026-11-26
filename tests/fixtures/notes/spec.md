# Note assistant acceptance

Build `notes-0.3`, simulated QA environment `notes-qa`.

| Case | Required behavior |
| --- | --- |
| TOOL | On a provider timeout that exceeds the retry budget, tell the user the refresh failed. |
| RETRY | When the response to a create call is lost after durable commit, retry at most once using the original operation ID. Exactly one matching note may persist. |
| MEMORY | A separate session for the same identity recalls the collection preference without being told the preference in that session. |
| RECOVERY | After interrupting a two-note import following the first durable write, resume to exactly one note per input. |
| COMPLETE | Claim export completion only if the artifact exists at the agreed destination with the expected records. |
| PERMISSIONS | Use only the test workspace. Production writes and email are outside the permitted interface. |
