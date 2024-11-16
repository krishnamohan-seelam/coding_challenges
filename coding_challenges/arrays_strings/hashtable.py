# coding: utf-8
# # Challenge Notebook

# ## Problem: Implement a hash table with set, get, and remove methods.
#
# * [Constraints](#Constraints)
# * [Test Cases](#Test-Cases)
# * [Algorithm](#Algorithm)
# * [Code](#Code)
# * [Unit Test](#Unit-Test)
# * [Solution Notebook](#Solution-Notebook)

# ## Constraints
#
# * For simplicity, are the keys integers only?
#     * Yes
# * For collision resolution, can we use chaining?
#     * Yes
# * Do we have to worry about load factors?
#     * No
# * Do we have to validate inputs?
#     * No
# * Can we assume this fits memory?
#     * Yes


class DataNode:
    def __init__(self, key: int, value):
        self.key = key
        self.value = value


class IntegerHashTable:

    def __init__(self, size):
        self.size = size
        self._array = [[] for i in range(self.size)]

    def _validate_key(self, key):
        if not isinstance(key, int):
            raise TypeError("Key must be an integer")

    def _hash_function(self, key):
        self._validate_key(key)
        return key % self.size

    def set(self, key, value):
        self._validate_key(key)
        hash_index = self._hash_function(key)
        for datanode in self._array[hash_index]:
            if datanode.key == key:
                datanode.value = value
                return
        self._array[hash_index].append(DataNode(key, value))

    def get(self, key):
        self._validate_key(key)
        hash_index = self._hash_function(key)
        for datanode in self._array[hash_index]:
            if datanode.key == key:
                return datanode.value
        raise KeyError("key not found")

    def remove(self, key):
        self._validate_key(key)
        hash_index = self._hash_function(key)
        for index, datanode in enumerate(self._array[hash_index]):
            if datanode.key == key:
                del self._array[hash_index][index]
                return
        raise KeyError("key not found")
