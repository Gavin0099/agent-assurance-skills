# I Tested AI Code Review With and Without Agent Skills

I wanted to know whether review instructions change what an AI finds once it has the same patch and evidence as every other reviewer. I also wanted to know whether a deterministic evidence report improves that comparison. The useful result was a gain in identifying CI records, alongside a reminder that an agent can still miss a real regression.

## What I compared

I used ten public PRs from packaging, Click and attrs, with 17 required review points written down before scoring. Those points included scope, test quality, clean changes and missing evidence. Four cases used historical intermediate revisions. The three arms used Claude Code 2.1.220 with Sonnet 5 (`claude-sonnet-5`) and fixed offline evidence. The baseline received the task and evidence. Community added the published review instructions, reference and template. Community plus Pro also received a locally generated report from the same snapshot. The model had no tools in these runs. An independent AI grader scored shuffled reports without the arm labels. Report style could still hint at the arm. [Pinned Community review instructions](https://github.com/Gavin0099/agent-assurance-skills/tree/bd53617b579dee09eb09781f1bffdc083540a100/skills/ai-pr-evidence-review)

| Ten primary PRs | Baseline | Community | Community + Pro |
| --- | ---: | ---: | ---: |
| Required review points met | 13/17 | 13/17 | 16/17 |
| Revision and evidence identity | 9/10 | 9/10 | 10/10 |
| Test assessment | 9/10 | 9/10 | 9/10 |
| Unsupported statements | 0 | 2 | 0 |
| Statements contradicted by evidence | 0 | 5 | 2 |

These are original aggregate scores for this comparison. Compared with Community, the Pro arm did better on three PRs, worse on one and tied on six. The aggregate score can hide different mistakes.

<details>
<summary>Scores and reviewed revisions for all ten PRs</summary>

| Public PR | Reviewed revision | Baseline | Community | Community + Pro |
| --- | --- | ---: | ---: | ---: |
| [packaging #1093](https://github.com/pypa/packaging/pull/1093) | [2fa545e](https://github.com/pypa/packaging/commit/2fa545e44739a33b06f28bdd46d1d512a94b2703) (intermediate) | 1/1 | 1/1 | 1/1 |
| [packaging #1097](https://github.com/pypa/packaging/pull/1097) | [f31d105](https://github.com/pypa/packaging/commit/f31d1050d6b8245cb4b7f7b61866948307fb5a95) (intermediate) | 1/2 | 0/2 | 2/2 |
| [packaging #1160](https://github.com/pypa/packaging/pull/1160) | [a7394c9](https://github.com/pypa/packaging/commit/a7394c9d9482e8abcdbd2f1eccfc781afac76797) | 1/2 | 1/2 | 2/2 |
| [packaging #1121](https://github.com/pypa/packaging/pull/1121) | [c147406](https://github.com/pypa/packaging/commit/c147406bd742d25d0fb33a6a885625edf422d0e6) | 1/1 | 1/1 | 1/1 |
| [packaging #1166](https://github.com/pypa/packaging/pull/1166) | [e32bfca](https://github.com/pypa/packaging/commit/e32bfca8ea512c5343be701c47ed8455e6798711) (intermediate) | 2/2 | 2/2 | 2/2 |
| [Click #2972](https://github.com/pallets/click/pull/2972) | [d1f8651](https://github.com/pallets/click/commit/d1f865142812584b9a1630106cce3f2309751e71) | 2/2 | 2/2 | 2/2 |
| [Click #3507](https://github.com/pallets/click/pull/3507) | [665736b](https://github.com/pallets/click/commit/665736bc85a19a7a2357c071394b4a545617faa3) | 2/2 | 2/2 | 2/2 |
| [Click #3509](https://github.com/pallets/click/pull/3509) | [82f377c](https://github.com/pallets/click/commit/82f377c547e1867d073f02bb8f476214d07e245b) | 1/1 | 1/1 | 1/1 |
| [attrs #1652](https://github.com/python-attrs/attrs/pull/1652) | [2cf7df2](https://github.com/python-attrs/attrs/commit/2cf7df2e50e8d21521ac00bfe74a1e0bdc900934) (intermediate) | 1/2 | 1/2 | 2/2 |
| [attrs #1663](https://github.com/python-attrs/attrs/pull/1663) | [225715e](https://github.com/python-attrs/attrs/commit/225715ee60870e21b28f4c35de6031cd85eab390) | 1/2 | 2/2 | 1/2 |

</details>

Mean input tokens per PR, including cache creation and reads, were 4,560 for baseline, 6,842 for Community and 7,903 for Community plus Pro. Mean model CLI elapsed times were 15.90, 20.72 and 18.94 seconds respectively. Pro also ran a local verifier for 0.20 seconds per PR on average. These are machine durations. Human review and correction minutes were unmeasured.

## Reproduce the regression one arm found

A separate historical Click case exposes the distinction between reading evidence and finding a behavioral fault. Click's prompt fix converted `StopIteration` into `EOFError` in the text wrapper. The wrapper was shared with ordinary line iteration, which expects exhaustion to terminate the loop. The miniature below models only the changed iterator protocol using the Python standard library. Save it as `check_eof.py` and run `python -B check_eof.py`.

```python
from io import BytesIO, TextIOWrapper


class CandidateStream(TextIOWrapper):
    def __next__(self):
        try:
            return super().__next__()
        except StopIteration as error:
            raise EOFError from error


for stream_type in (TextIOWrapper, CandidateStream):
    lines = []
    try:
        with stream_type(BytesIO(b"one\ntwo\n"), encoding="utf-8") as stream:
            for line in stream:
                lines.append(line.strip())
    except EOFError:
        print(lines, "EOFError")
    else:
        print(lines, "normal termination")
```

Both yield `['one', 'two']`. The first ends normally. The second raises `EOFError` when the loop asks for the next line. Click's follow-up scoped the conversion to prompt handling. In this separately scored case Community met 3/3 required points and the other two arms met 1/3 each. Only Community named the normal stdin iteration failure. This example exercises the stream protocol and leaves the upstream Click suite unexecuted. [Original change](https://github.com/pallets/click/commit/262bdf02288daf9a37b9e815b44acafd62b5c6fe) · [Upstream fix](https://github.com/pallets/click/commit/93c6966eb3a575c2b600434d1cc9f4b3aee505ac)

The study used one model, ten selected PRs and an offline evidence packet for each. The 17 points are broader than defect detection. There was no measurement of human review minutes, end-to-end collection savings or purchase value. I would use the extra evidence report to keep CI provenance straight and still read the source and tests for behavior.

**Disclosure.** I create and sell Agent Assurance products and ran this comparison on my own tools. AI assisted with drafting and checking this article. [GitHub Community](https://github.com/Gavin0099/agent-assurance-skills/releases/tag/v0.1.0) · [Gumroad Pro](https://reikoshine.gumroad.com/l/vwihs)
