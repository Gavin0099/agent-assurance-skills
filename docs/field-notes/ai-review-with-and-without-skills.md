# I Tested AI Code Review With and Without Agent Skills

I wanted to know whether review instructions change what an AI finds once it has the same patch and evidence as every other reviewer. I also wanted to know whether a deterministic evidence report improves that comparison. The useful result was a gain in identifying CI records, alongside a reminder that an agent can still miss a real regression.

## What I compared

I used ten public PRs from packaging, Click and attrs, with 17 required review points written down before scoring. Those points included scope, test quality, clean changes and missing evidence. Four cases used historical intermediate revisions. The three arms used the same Claude Code model and fixed offline evidence. The baseline received the task and evidence. Community added the published review instructions, reference and template. Community plus Pro also received a locally generated report from the same snapshot. The model had no tools in these runs. An independent AI grader scored shuffled reports without the arm labels. Report style could still hint at the arm. [Pinned Community review instructions](https://github.com/Gavin0099/agent-assurance-skills/tree/bd53617b579dee09eb09781f1bffdc083540a100/skills/ai-pr-evidence-review)

| Ten primary PRs | Baseline | Community | Community + Pro |
| --- | ---: | ---: | ---: |
| Required review points met | 13/17 | 13/17 | 16/17 |
| Revision and evidence identity | 9/10 | 9/10 | 10/10 |
| Test assessment | 9/10 | 9/10 | 9/10 |
| Unsupported statements | 0 | 2 | 0 |
| Statements contradicted by evidence | 0 | 5 | 2 |

These are original aggregate scores for this comparison. Compared with Community, the Pro arm did better on three PRs, worse on one and tied on six. Agreed aggregate scores do not mean reviewers made the same mistakes.

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
