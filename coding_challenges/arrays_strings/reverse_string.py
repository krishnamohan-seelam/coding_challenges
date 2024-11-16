"""
# ## Problem: Implement a function to reverse a string (a list of characters), in-place.
# 
# ## Constraints
# 
# * Can we assume the string is ASCII?
#     * Yes
#     * Note: Unicode strings could require special handling depending on your language
# * Since we need to do this in-place, it seems we cannot use the slice operator or the reversed function?
#     * Correct
# * Since Python string are immutable, can we use a list of characters instead?
#     * Yes

# ## Test Cases
# 
# * None -> None
# * [''] -> ['']
# * ['f', 'o', 'o', ' ', 'b', 'a', 'r'] -> ['r', 'a', 'b', ' ', 'o', 'o', 'f']
"""


class ReverseString(object):

    def reverse(self, chars):
        # TODO: Implement me
        if chars is None or len(chars) == 0:
            return chars
        result = []
        chars_len = len(chars)
        while chars_len > 0:
            result.append(chars[chars_len - 1])
            chars_len -= 1
        return result


if __name__ == "__main__":
    rs = ReverseString()
    result = rs.reverse(["f", "o", "o", "b", "a", "r"])
    print(result)
