import unittest
from main import sort_alphanumeric_string


class TestSortAlphanumericString(unittest.TestCase):
    def test_sort_alphanumeric_string(self):
        # Testing with valid input
        self.assertEquals(
            sort_alphanumeric_string("dsfsfhj1231ADS"),
            ["d", "f", "f", "h", "j", "s", "s", "A", "D", "S", "1", "1", "3", "2"],
        )
