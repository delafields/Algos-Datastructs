'''
Implement a hash table with get, set, remove

Constraints
    For simplicity, keys are integers only
    For collision resolution, use chaining
    Do not worry about load factors
    Do not need to validate inputs
    Assume this fits in memory

Test Cases
    'get' not matching key -> KeyError exception
    'get' matching key -> value
    'set' no matching key -> new key, value
    'set' matching key -> update value
    'remove' no matching key -> KeyError exception
    'remove' matching key -> remove key, value
'''
# Implement
class Item:

    def __init__(self, key, value):
        # TODO: Implement me
        pass


class HashTable:

    def __init__(self, size):
        # TODO: Implement me
        pass

    def _hash_function(self, key):
        # TODO: Implement me
        pass

    def set(self, key, value):
        # TODO: Implement me
        pass

    def get(self, key):
        # TODO: Implement me
        pass

    def remove(self, key):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal, assert_raises


class TestHashMap(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        hash_table = HashTable(10)

        print("Test: get on an empty hash table index")
        assert_raises(KeyError, hash_table.get, 0)

        print("Test: set on an empty hash table index")
        hash_table.set(0, 'foo')
        assert_equal(hash_table.get(0), 'foo')
        hash_table.set(1, 'bar')
        assert_equal(hash_table.get(1), 'bar')

        print("Test: set on a non empty hash table index")
        hash_table.set(10, 'foo2')
        assert_equal(hash_table.get(0), 'foo')
        assert_equal(hash_table.get(10), 'foo2')

        print("Test: set on a key that already exists")
        hash_table.set(10, 'foo3')
        assert_equal(hash_table.get(0), 'foo')
        assert_equal(hash_table.get(10), 'foo3')

        print("Test: remove on a key that already exists")
        hash_table.remove(10)
        assert_equal(hash_table.get(0), 'foo')
        assert_raises(KeyError, hash_table.get, 10)

        print("Test: remove on a key that doesn't exist")
        assert_raises(KeyError, hash_table.remove, -1)

        print('Success: test_end_to_end')


def main():
    test = TestHashMap()
    test.test_end_to_end()


if __name__ == '__main__':
    main()


'''
Algorithm
    Hash Function
        Return key % table size
        Complexity:
            Time: O(1)
            Space: O(1)

    Set
        Get hash index for lookup
        If key exists, replace
        Else, add
        Complexity:
            Time: O(1) avg and best, O(n) worst
            Space: O(1) space for newly added element

    Get
        Get hash index for lookup
        If key exists, return value
        Else, raise KeyError
        Complexity:
            Time: O(1) avg and best, O(n) worst
            Space: O(1)

    Remove
        Get hash index for lookup
        If key exists, delete the item
        Else, raise KeyError
        Complexity:
            Time: O(1) avg and best, O(n) worst
            Space: O(1)
'''
# Solution

class ItemSolution:

    def __init__(self, key, value):
        self.key = key
        self.value = value

class HashTableSolution:

    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(self.size)]

    def _hash_function(self, key):
        return key % self.size

    def set(self, key, value):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                item.value = value
                return
        self.table[hash_index].append(Item(key, value))

    def get(self, key):
        hash_index = self._hash_function(key)
        for item in self.table[hash_index]:
            if item.key == key:
                return item.value
        raise KeyError('Key not found')

    def remove(self, key):
        hash_index = self._hash_function(key)
        for item, index in enumerate(self.table[hash_index]):
            if item.key == key:
                del self.table[hash_index][index]
                return
        raise KeyError('Key not found')
