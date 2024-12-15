# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Find the kth to last element of a linked list.
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
# * Can we assume k is a valid integer?
#     * Yes
# * If k = 0, does this return the last element?
#     * Yes
# * What happens if k is greater than or equal to the length of the linked list?
#     * Return None
# * Can you use additional data structures?
#     * No
# * Can we assume we already have a linked list class that can be used for this problem?
#     * Yes

# ## Test Cases
#
# * Empty list -> None
# * k is >= the length of the linked list -> None
# * One element, k = 0 -> element
# * General case with many elements, k < length of linked list

from coding_challenges.linked_lists.linkedlist import LinkedList


class KthToLastElementLL(LinkedList):

    def kth_to_last_elem(self, k):
        if self.head is None:
            return None
        len_of_list = len(self)
        if k >= len_of_list:
            return None
        if len_of_list == 1:
            return self.head.data

        return self.get(k)
