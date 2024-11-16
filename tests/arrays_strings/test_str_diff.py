import unittest
from coding_challenges.arrays_strings.str_diff import StrDiff


class TestStrDiff(unittest.TestCase):

    def test_str_diff(self):
        strdiff = StrDiff()
        with self.assertRaises(TypeError):
            test_result = strdiff.find_diff(None, None)
        self.assertEqual(strdiff.find_diff("ab", "aab"), "a")
        self.assertEqual(strdiff.find_diff("aab", "ab"), "a")
        self.assertEqual(strdiff.find_diff("abcd", "abcde"), "e")
        self.assertEqual(strdiff.find_diff("aaabbcdd", "abdbacade"), "e")
