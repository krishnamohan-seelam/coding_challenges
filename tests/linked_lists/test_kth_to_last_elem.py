from coding_challenges.linked_lists.kth_to_last_element import KthToLastElementLL
from coding_challenges.linked_lists.linkedlist import Node
import unittest


class Testkth_to_last_element(unittest.TestCase):

    def test_kth_to_last_element(self):
        linked_list = KthToLastElementLL(None)
        self.assertEqual(linked_list.kth_to_last_elem(0), None)
        self.assertEqual(linked_list.kth_to_last_elem(100), None)
        head = Node(2)
        linked_list2 = KthToLastElementLL(head)
        self.assertEqual(linked_list2.kth_to_last_elem(0), 2)
        linked_list2.insert_to_front(1)
        linked_list2.insert_to_front(3)
        linked_list2.insert_to_front(5)
        linked_list2.insert_to_front(7)
        self.assertEqual(linked_list2.kth_to_last_elem(2), 3)
