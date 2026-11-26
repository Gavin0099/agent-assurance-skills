# Why Deterministic Verification Matters for AI Agents

Two GitHub Actions jobs in packaging PR #1160 had the same label, `Ubuntu / 3.12`, and both reported success. Only one job belonged to the revision under review. A review that quotes the label and says “CI passed” leaves a reader unable to tell which record it used.

The difference was in the identity fields. Job `71395298899` reported success on `43106f7739a2245c55acf2f5023c6548408d7adc`. Job `71397417876` reported success on the selected candidate, `a7394c9d9482e8abcdbd2f1eccfc781afac76797`. This is a historical comparison pinned to the candidate commit. [Candidate commit](https://github.com/pypa/packaging/commit/a7394c9d9482e8abcdbd2f1eccfc781afac76797) · [Earlier job](https://github.com/pypa/packaging/actions/runs/24437627683/job/71395298899?pr=1160) · [Candidate job](https://github.com/pypa/packaging/actions/runs/24438320949/job/71397417876?pr=1160)

## Turn the identity question into code

Save the following as `bind_ci.py` and run `python -B bind_ci.py`. The two rows transcribe the observed job identifiers, revisions and conclusions. The third is a synthetic negative control. The example is self-contained and needs no token, API request or paid tool.

```python
target = "a7394c9d9482e8abcdbd2f1eccfc781afac76797"
rows = [
    (71395298899, "43106f7739a2245c55acf2f5023c6548408d7adc", "success"),
    (71397417876, "a7394c9d9482e8abcdbd2f1eccfc781afac76797", "success"),
    ("synthetic-missing-sha", None, "success"),
]

for job_id, observed_sha, reported_conclusion in rows:
    binding = "UNKNOWN"
    if observed_sha is not None:
        binding = "MATCH" if observed_sha == target else "MISMATCH"
    print(job_id, binding, reported_conclusion)
```

The output is:

```text
71395298899 MISMATCH success
71397417876 MATCH success
synthetic-missing-sha UNKNOWN success
```

The last column is what the source reported. The binding column answers whether that report applies to the selected revision. Keep both columns even when every check is green. Record the repository, provider and run identity alongside the SHA in production. If CI tested an integration commit, compare the tested commit and its parent revisions. A matched job can still leave questions about which test cases ran and whether they detect the failure you care about. [GitHub check-run inputs and response](https://docs.github.com/en/rest/checks/runs)

## What changed in three repetitions

In a fixed offline comparison I repeated this PR three times per arm with the same model. The baseline and Community reviewers distinguished earlier and current SHAs but each run omitted at least one of the two required job IDs. Each scored 1/2 in all three runs. Community plus Pro had the two identities and applicability decisions in its generated evidence report and scored 2/2 each time. The rubric counted the IDs because repeating the job label alone did not identify either result. This is one PR, one model and one kind of ambiguity. Across ten primary PRs the revision-and-evidence score went from 9/10 with Community to 10/10 with Community plus Pro.

A structured report helps reviewers check identity and preserve missing evidence. Its guarantees depend on the inputs. The toy example trusts its transcribed rows. An offline verifier can compare those identifiers without authenticating their origin. The trial did not establish human time savings or a general increase in defect detection.

**Disclosure.** I create and sell Agent Assurance products. AI assisted with drafting and checking this article. The example above uses public evidence and Python alone. [GitHub Community](https://github.com/Gavin0099/agent-assurance-skills/releases/tag/v0.1.0) · [Gumroad Pro](https://reikoshine.gumroad.com/l/vwihs)
