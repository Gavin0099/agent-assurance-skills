import unittest

from delivery import estimated_minutes


class DeliveryTest(unittest.TestCase):
    def test_estimate_aligned(self):
        self.assertEqual(estimated_minutes(30), 30)
