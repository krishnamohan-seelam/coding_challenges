from coding_challenges.arrays_strings.permutations import Permutations


import unittest


class TestPermutation(unittest.TestCase):

    def test_permutation(self):
        p = Permutations()
        self.assertEqual(p.is_permutation(None, "foo"), False)
        self.assertEqual(p.is_permutation("", "foo"), False)
        self.assertEqual(p.is_permutation("Nib", "bin"), False)
        self.assertEqual(p.is_permutation("act", "cat"), True)
        self.assertEqual(p.is_permutation("a ct", "ca t"), True)
        self.assertEqual(p.is_permutation("dog", "doggo"), False)
        print("Success: test_permutation")
