'''
Implement a Priority Queue backed by an array

Constraints
    Methods: insert, extract_min and decrease_key
    Assume there are no duplicate keys
    We do not need to validate inputs
    Assume it fits in memory

Test Cases
    insert
        Insert general case -> inserted node
    extract_min
        extract_min from an empty list -> None
        extract_min general case -> min node
    decrease_key
        decrease_key an invalid key -> None
        decrease_key general case -> updated node
'''
# Implement
class PriorityQueueNode:

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)


class PriorityQueue:

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        # TODO: Implement me
        pass

    def extract_min(self):
        # TODO: Implement me
        pass

    def decrease_key(self, obj, new_key):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestPriorityQueue(object):

    def test_priority_queue(self):
        priority_queue = PriorityQueue()
        assert_equal(priority_queue.extract_min(), None)
        priority_queue.insert(PriorityQueueNode('a', 20))
        priority_queue.insert(PriorityQueueNode('b', 5))
        priority_queue.insert(PriorityQueueNode('c', 15))
        priority_queue.insert(PriorityQueueNode('d', 22))
        priority_queue.insert(PriorityQueueNode('e', 40))
        priority_queue.insert(PriorityQueueNode('f', 3))
        priority_queue.decrease_key('f', 2)
        priority_queue.decrease_key('a', 19)
        mins = []
        while priority_queue.array:
            mins.append(priority_queue.extract_min().key)
        assert_equal(mins, [2, 5, 15, 19, 22, 40])
        print('Success: test_min_heap')


def main():
    test = TestPriorityQueue()
    test.test_priority_queue()


if __name__ == '__main__':
    main()

'''
Algorithm
    insert
        Append to the internal array
        Complexity:
            Time: O(1)
            Space: O(1)

    extract_min
        Loop through each item in the internal array
            Update the min value as needed
        Remove the min element from the array and return it
        Complexity:
            Time: O(n)
            Space: O(1)

    decrease_key
        Loop through each item in the internal array to find the matching input
            Update the matching element's key
        Complexity:
            Time: O(n)
            Space: O(1)
'''
# Solution
import sys

class PriorityQueueNodeSolution:

    def __init__(self, obj, key):
        self.obj = obj
        self.key = key

    def __repr__(self):
        return str(self.obj) + ': ' + str(self.key)

class PriorityQueueSolution:

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def insert(self, node):
        self.array.append(node)
        return self.array[-1]

    def extract_min(self):
        if not self.array:
            return None
        minimum = sys.maxsize
        for index, node in enumerate(self.array):
            if node.key < minimum:
                minimum = node.key
                minimum_index = index
        return self.array.pop(minimum_index)

    def decrease_key(self, obj, new_key):
        for node in self.array:
            if node.obj is obj:
                node.key = new_key
                return node
        return None
