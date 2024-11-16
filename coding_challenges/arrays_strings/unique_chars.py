"""
# ## Problem: Implement an algorithm to determine if a string has all unique characters.
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
# * Can we assume this is case sensitive?
#     * Yes
# * Can we use additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * None -> False
# * '' -> True
# * 'foo' -> False
# * 'bar' -> True
"""


class UniqueChars(object):

    def has_unique_chars(self, in_data):
        if not isinstance(in_data, str):
            return False
        return len(set(in_data)) == len(in_data)
