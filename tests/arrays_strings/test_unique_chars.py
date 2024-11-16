import unittest
from coding_challenges.arrays_strings.unique_chars import UniqueChars


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self):
        unique_chars = UniqueChars()
        self.assertEqual(unique_chars.has_unique_chars(None), False)
        self.assertEqual(unique_chars.has_unique_chars(""), True)
        self.assertEqual(unique_chars.has_unique_chars("foo"), False)
        self.assertEqual(unique_chars.has_unique_chars("bar"), True)
        print("Success: test_unique_chars")
