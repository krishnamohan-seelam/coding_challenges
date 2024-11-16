import unittest
from coding_challenges.arrays_strings.compress_string import CompressString


class TestUniqueChars(unittest.TestCase):

    def test_unique_chars(self):
        compress_string = CompressString()
        self.assertEqual(compress_string.compress(None), None)
        self.assertEqual(compress_string.compress(""), "")
        self.assertEqual(compress_string.compress("AABBCC"), "AABBCC")
        self.assertEqual(compress_string.compress("AAABCCDDDDE"), "A3BC2D4E")
        self.assertEqual(compress_string.compress("BAAACCDDDD"), "BA3C2D4")
        self.assertEqual(compress_string.compress("AAABAACCDDDD"), "A3BA2C2D4")
        print("Success: test_unique_chars")


# def main():
#     test = TestUniqueChars()
#     unique_chars = UniqueChars()
#     test.test_unique_chars(unique_chars.has_unique_chars)
#     # try:
#     #     unique_chars_set = UniqueCharsSet()
#     #     test.test_unique_chars(unique_chars_set.has_unique_chars)
#     #     unique_chars_in_place = UniqueCharsInPlace()
#     #     test.test_unique_chars(unique_chars_in_place.has_unique_chars)
#     # except NameError:
#     #     # Alternate solutions are only defined
#     #     # in the solutions file
#     #     pass


# if __name__ == "__main__":
#     main()
