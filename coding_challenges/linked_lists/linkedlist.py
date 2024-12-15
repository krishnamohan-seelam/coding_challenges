# coding: utf-8

# This notebook was prepared by [Donne Martin](http://donnemartin.com). Source and license info is on [GitHub](https://github.com/donnemartin/interactive-coding-challenges).

# # Challenge Notebook

# ## Problem: Implement a linked list with insert, append, find, delete, length, and print methods.

import copy


class Node(object):

    def __init__(self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def __str__(self):
        return str(self.data)

    def __repr__(self):
        return repr(self.data)


class LinkedList(object):

    def __init__(self, head: Node = None):
        self.head = head

    def __len__(self):
        """
        __len__  - _summary_

        _extended_summary_
        """
        return len(self.traverse())

    def get(self, index):
        """
        Get the data at the given index.

        Parameters:
            index (int): The index of the element to retrieve, starting from the head of the list.

        Returns:
            Any: A deep copy of the data at the given index if found.

        Error Handling:
            Raising an IndexError if index is invalid.
        """
        if index < 0:
            raise IndexError("Index must be non-negative")
        current = self.head
        current_index = 0
        while current_index < index and current is not None:
            current = current.next_node
            current_index += 1
        if current is None:
            raise IndexError("Index out of bounds")
        # Here we know that we are at the right index
        return copy.deepcopy(current.data)

    def __iter__(self):
        """
        __iter__  - Iterates over the values in linked list

        Iterations starts from beginning of the linked list until it reaches the end
        """
        current = self.head
        while current is not None:
            value = current.data
            current = current.next_node
            yield value

    def traverse(self, functor=None):
        """
        traverse  - Iterates over the linked list and applies function on the data from each node
        """
        result = []
        for data in iter(self):
            value = functor(data) if functor else data
            result.append(value)
        return result

    def insert_to_front(self, data):
        if data is None:
            return None

        if self.head is None:
            self.head = Node(data)
        else:
            prev_head = self.head
            self.head = Node(data, prev_head)
        return self.head

    def append(self, data):
        if data is None:
            return None

        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return new_node
        current = self.head
        while current.next_node is not None:
            current = current.next_node
        current.next_node = new_node
        return new_node

    def find(self, data):
        if data is None or self.head is None:
            return None
        current = self.head
        while current is not None:
            if current.data == data:
                return current
            current = current.next_node

    def delete(self, data):
        if data is None or self.head is None:
            return None
        current = self.head
        previous = None
        while current is not None:
            if current.data == data:
                if previous is None:
                    self.head = current.next_node
                else:
                    previous.next_node = current.next_node
                return data
            previous = current
            current = current.next_node
        raise ValueError(f"No element with value {data} was found in the list.")

    def __str__(self):
        """
        __str__  Return the string representation of the linked list.

        """
        return "->".join(str(x) for x in iter(self))

    def print_list(self):
        return str(self)

    def get_all_data(self):
        return self.traverse()


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_to_front(1)
    ll.insert_to_front(3)
    ll.insert_to_front(5)
    ll.insert_to_front(7)
    el = ll.get(0)
    print(el)
