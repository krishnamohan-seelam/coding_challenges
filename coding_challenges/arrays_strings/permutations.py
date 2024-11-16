"""
# ## Problem: Determine if a string is a permutation of another string.
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
# * Is whitespace important?
#     * Yes
# * Is this case sensitive?  'Nib', 'bin' is not a match?
#     * Yes
# * Can we use additional data structures?
#     * Yes
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
# 
# * One or more None inputs -> False
# * One or more empty strings -> False
# * 'Nib', 'bin' -> False
# * 'act', 'cat' -> True
# * 'a ct', 'ca t' -> True
"""

import itertools


class Permutations(object):

    def is_permutation(self, str1, str2):
        # TODO: Implement me
        if str1 is None or str2 is None:
            return False
        x = itertools.permutations(list(str1), len(str1))
        y = set("".join(t) for t in x)
        return str2 in y
