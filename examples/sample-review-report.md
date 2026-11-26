# PR evidence review — Delivery estimate rounding

## Review target

Example fixture. The ticket asks for quarter-hour rounding without changing the free-delivery threshold. The report uses symbolic revisions `H1` and `H2` to describe a head change in the example. The reviewed head was `H1` and the head at report time was `H2`. **Current-head verification is BLOCKED.**

## Findings at H1

- **Medium · `delivery.py:6`** — The minimum free-delivery subtotal increased from 5,000 to 6,000 cents. An order with a subtotal of 5,500 cents now pays delivery, which violates the ticket. Static reproduction is to pass `5500` to `is_free_delivery` and compare the return value on base and H1. Execution was outside this review.
- **Medium · `test_delivery.py:8`** — The only rounding test supplies 30 minutes, which is already aligned to a quarter hour. The test passes against the prior identity implementation and does not exercise the ticket's 31-minute example.

## Requirement and test coverage

| Requirement | Inspected evidence | Gap |
| --- | --- | --- |
| Round up to the next quarter-hour | `test_estimate_aligned` asserts 30 → 30 | 31 → 45 and boundary assertions are missing. |
| Preserve free delivery at 5,000 cents | Candidate source changed the threshold | No test exercises the original threshold. |

## Verification evidence

The supplied CI run succeeded on `H1` and executed one rounding test. It is stale for `H2`. No run was supplied for `H2`.

## Suggested next action

Review `H2` and obtain matching CI evidence. Verify threshold preservation and add a test that fails on the prior rounding behavior.
