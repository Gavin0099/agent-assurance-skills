# Why a green CI check can miss a PR regression

A delivery estimate change had one passing test and a six-line implementation. The ticket asked for quarter-hour rounding while keeping free delivery at 5,000 cents. At the reviewed commit, a 5,500-cent order unexpectedly paid for delivery.

This was a synthetic pull request fixture. Its CI receipt represents a local test the fixture preparer ran, so we can trace exactly what the green check established. [Fixture and setup](../tests/evaluations/README.md)

## Read the assertion

The only test asserted that 30 minutes still displays as 30. Thirty is already a multiple of 15, so the old implementation, which returns its input unchanged, passes too. The ticket's 31-minute example separates the implementations. The old code returns 31 and the candidate returns 45.

The existing test exercises a boundary where both implementations agree. A 31 → 45 assertion would demonstrate the new behavior while retaining the 30 → 30 assertion to check the aligned case. [Ticket](../tests/fixtures/delivery/ticket.md) · [Candidate test](../tests/fixtures/delivery/candidate/test_delivery.py)

## Check what the ticket asked to preserve

The ticket also holds the free-delivery threshold at 5,000 cents. At H1 the threshold changed to 6,000. A 5,500-cent subtotal is enough to show the effect from the source. In the base version it qualifies. At H1 it falls below the new threshold. The sole rounding test never calls the free-delivery function. [Candidate implementation](../tests/fixtures/delivery/candidate/delivery.py)

## Match the check to the current commit

The supplied green receipt records H1 and one executed test. The branch later moves to H2, where the fixture restores the threshold. The H1 result still describes H1. With no H2 test record, current-commit verification remains blocked. The revised code can support a source-level finding about the threshold while the CI evidence stays attached to the commit that ran it. [Sample review](../examples/sample-review-report.md)

On your next review, ask for the tested commit, the assertions the run executed, and one example that would fail on the old implementation. Those details turn a green status into evidence you can evaluate against the ticket.
