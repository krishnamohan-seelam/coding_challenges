# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Remove duplicates from a linked list.
#
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
#
# * Can we assume this is a non-circular, singly linked list?
#     * Yes
# * Can you insert None values in the list?
#     * No
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes
# * Can we use additional data structures?
#     * Implement both solutions
# * Can we assume this fits in memory?
#     * Yes

# ## Test Cases
#
# * Empty linked list -> []
# * One element linked list -> [element]
# * General case with no duplicates
# * General case with duplicates
from coding_challenges.linked_lists.linkedlist import LinkedList


class RemoveDuplicates(LinkedList):

    def remove_dupes(self):
        # TODO: Implement me
        seen = set()
        if self.head is None:
            return None
        current = self.head
        prev = None
        while current is not None:
            if current.data not in seen:
                seen.add(current.data)
                prev = current
                current = current.next_node
            else:
                prev.next_node = current.next_node
                current = current.next_node
