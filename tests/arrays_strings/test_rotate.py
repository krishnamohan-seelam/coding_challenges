import unittest
from coding_challenges.arrays_strings.rotate import Rotation


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self):
        rotation = Rotation()
        self.assertEqual(rotation.is_rotation("o", "oo"), False)
        self.assertEqual(rotation.is_rotation(None, "foo"), False)
        self.assertEqual(rotation.is_rotation("", "foo"), False)
        self.assertEqual(rotation.is_rotation("", ""), True)
        self.assertEqual(rotation.is_rotation("foobarbaz", "barbazfoo"), True)
        print("Success: test_rotation")
        print("Success: test_unique_chars")
