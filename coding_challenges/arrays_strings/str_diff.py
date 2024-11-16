# coding: utf-8

# This notebook was prepared by [Donne Martin](https://github.com/donnemartin). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the single different char between two strings.
#
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
#
# * Can we assume the strings are ASCII?
#     * Yes
# * Is case important?
#     * The strings are lower case
# * Can we assume the inputs are valid?
#     * No, check for None
#     * Otherwise, assume there is only a single different char between the two strings
# * Can we assume this fits memory?
#     * Yes

# ## Test Cases
#
# * None input -> TypeError
# * 'ab', 'aab' -> 'a'
# * 'aab', 'ab' -> 'a'
# * 'abcd', 'abcde' -> 'e'
# * 'aaabbcdd', 'abdbacade' -> 'e'


class StrDiff:

    def find_diff(self, str1, str2):
        # TODO: Implement me
        if str1 is None or str2 is None:
            raise TypeError("invalid string")
        char_seen = {}
        for char in str1:
            if char in char_seen:
                char_seen[char] += 1
            else:
                char_seen[char] = 1

        for char in str2:
            try:
                char_seen[char] -= 1
            except KeyError:
                return char
            if char_seen[char] < 0:
                return char
        for char, count in char_seen.items():
            if count >= 1:
                return char


def run():
    sd = StrDiff()
    r = sd.find_diff("aaabbcdd", "abdbacade")
    print(r)


if __name__ == "__main__":
    run()
