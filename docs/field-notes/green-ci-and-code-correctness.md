# Why Green CI Doesn’t Mean Your AI-Generated Code Is Correct

The ticket asked for two things. Round delivery estimates up to the next quarter hour and keep free delivery at 5,000 cents. The candidate had a green check for its one test. A 5,500-cent order nevertheless lost free delivery.

This is a deliberately small fixture from Agent Assurance Community. It makes it possible to see which assertion passed, which requirement went untested, and which revision the receipt describes. The review technique applies regardless of who wrote the code. [Pinned ticket and fixture](https://github.com/Gavin0099/agent-assurance-skills/tree/bd53617b579dee09eb09781f1bffdc083540a100/tests/fixtures/delivery)

## Run the same assertion against two implementations

Use Python 3 and Git. From a fresh checkout, run the candidate's test against both implementations. Only the candidate test file is loaded. The second command uses the base implementation.

```sh
git clone https://github.com/Gavin0099/agent-assurance-skills.git
cd agent-assurance-skills
git checkout --detach bd53617b579dee09eb09781f1bffdc083540a100
python -B -c "import sys,unittest; sys.path[:0]=['tests/fixtures/delivery/candidate']; unittest.main(module='test_delivery',argv=['unittest'])"
python -B -c "import sys,unittest; sys.path[:0]=['tests/fixtures/delivery/base','tests/fixtures/delivery/candidate']; unittest.main(module='test_delivery',argv=['unittest'])"
```

Both runs report one passing test. That test checks 30 → 30, and 30 is already aligned to a 15-minute boundary. Print a value that separates the implementations, plus an order subtotal that checks the preservation requirement.

```sh
python -B -c "import sys; sys.path.insert(0,'tests/fixtures/delivery/base'); from delivery import estimated_minutes,is_free_delivery; print(estimated_minutes(31),is_free_delivery(5500))"
python -B -c "import sys; sys.path.insert(0,'tests/fixtures/delivery/candidate'); from delivery import estimated_minutes,is_free_delivery; print(estimated_minutes(31),is_free_delivery(5500))"
```

The base prints `31 True`. The candidate prints `45 False`. The candidate implements the rounding requirement and violates the free-delivery requirement. An assertion for 31 → 45 would detect the rounding change. A separate assertion for a 5,500-cent order would catch the threshold regression.

## Ask which code the green check tested

The fixture's original success receipt describes H1 and one executed test. The reported head later moves to H2, where the threshold is restored. A source read supports that restoration. An H1 receipt can only establish what ran at H1. The sample report marks current-head verification blocked until there is H2 evidence. In GitHub Actions a `pull_request` workflow may test GitHub's merge ref, so record the commit actually checked out and its relationship to the candidate and base. [Pinned sample report](https://github.com/Gavin0099/agent-assurance-skills/blob/bd53617b579dee09eb09781f1bffdc083540a100/examples/sample-review-report.md) · [GitHub workflow event reference](https://docs.github.com/en/actions/reference/workflows-and-actions/events-that-trigger-workflows#pull_request)

For each claim in a review, keep three facts together: the requirement, an input that distinguishes compliant from broken behavior, and the execution receipt for the selected revision. The two comparisons above are observations from a synthetic fixture. They do not estimate how frequently teams encounter weak tests or stale CI.

**Disclosure.** I create and sell Agent Assurance products. AI assisted with drafting and checking this article. The examples are free to run. [GitHub Community](https://github.com/Gavin0099/agent-assurance-skills/releases/tag/v0.1.0) · [Gumroad Pro](https://reikoshine.gumroad.com/l/vwihs)
