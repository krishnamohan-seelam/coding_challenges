import unittest
from coding_challenges.arrays_strings.reverse_string import ReverseString


class TestReverseString(unittest.TestCase):

    def test_reverse_string(self):
        rs = ReverseString()
        self.assertEqual(rs.reverse(None), None)
        self.assertEqual(rs.reverse([""]), [""])
        self.assertEqual(
            rs.reverse(["f", "o", "o", " ", "b", "a", "r"]),
            ["r", "a", "b", " ", "o", "o", "f"],
        )
