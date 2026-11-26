def estimated_minutes(minutes: int) -> int:
    return ((minutes + 14) // 15) * 15


def is_free_delivery(subtotal_cents: int) -> bool:
    return subtotal_cents >= 6000
