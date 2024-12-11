from coding_challenges.linked_lists.remove_duplicates import RemoveDuplicates
import unittest


class TestRemoveDuplicates(unittest.TestCase):

    def test_remove_dupes(self):
        linked_list = RemoveDuplicates(None)
        print("Test: Empty list")
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [])

        print("Test: One element list")
        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [2])

        print("Test: General case, duplicates")
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print("Test: General case, no duplicates")
        linked_list.remove_dupes()
        self.assertEqual(linked_list.get_all_data(), [1, 3, 2])

        print("Success: test_remove_dupes\n")
