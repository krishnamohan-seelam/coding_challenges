"""
# ## Problem: Implement a function to reverse a string (a list of characters), in-place.
# 
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

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


class Rotation(object):

    def is_substring(self, s1, s2):
        # TODO: Implement me
        pass

    def is_rotation(self, s1, s2):
        # TODO: Implement me
        # Call is_substring only once
        if s1 is None or s2 is None:
            return False
        if len(s1) != len(s2):
            return False
        if s1 == s2:
            return True
        for counter in range(len(s1)):
            counter = counter % len(s1)
            v = s1[counter:] + s1[:counter]
            if v == s2:
                return True
        return False
