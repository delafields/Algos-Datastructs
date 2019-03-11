'''
Implement a min heap with extract_min and insert methods

Constraints
    Assume the inputs are ints
    Assume it fits in memory

Test Cases
    Extract min of an empty tree
    Extract min general case
    Insert into an empty tree
    Insert general case (left and right insert)
          _5_
        /     \
       20     15
      / \    /  \
     22  40 25

extract_min(): 5

          _15_
        /      \
       20      25
      / \     /  \
     22  40

insert(2):

          _2_
        /     \
       20      5
      / \     / \
     22  40  25  15
'''

# Implement
class MinHeap:

    def __init__(self):
        # TODO: Implement me
        pass

    def extract_min(self):
        # TODO: Implement me
        pass

    def peek_min(self):
        # TODO: Implement me
        pass

    def insert(self, data):
        # TODO: Implement me
        pass

    def _bubble_up(self, index):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestMinHeap(object):

    def test_min_heap(self):
        heap = MinHeap()
        assert_equal(heap.peek_min(), None)
        assert_equal(heap.extract_min(), None)
        heap.insert(20)
        assert_equal(heap.peek_min(), 20)
        heap.insert(5)
        assert_equal(heap.peek_min(), 5)
        heap.insert(15)
        heap.insert(22)
        heap.insert(40)
        heap.insert(5)
        assert_equal(heap.peek_min(), 5)
        heap.insert(3)
        assert_equal(heap.peek_min(), 3)
        assert_equal(heap.extract_min(), 3)
        assert_equal(heap.peek_min(), 5)
        print('Success: test_min_heap')


def main():
    test = TestMinHeap()
    test.test_min_heap()


if __name__ == '__main__':
    main()

'''
Algorithm
    A heap is a complete binary tree where each node is smaller than its children

    extract_min
             _5_
            /    \
          20     15
         / \    /  \
        22  40 25

        Save the root as the value to be returned: 5
        Move the right most element to the root: 25

             _25_
            /    \
          20     15
         / \    /  \
        22  40

        Bubble down 25: Swap 25 and 15 (smaller child)

             _15_
            /    \
          20     25
         / \    /  \
        22 40

        Return 5

        We'll use an array to represent the tree, here are the indices
            _0_
           /   \
          1     2
         / \   / \
        3   4
        To get a child, we take 2*index+1 (left child) or 2*index+2 (right child)
        For example, the right child of index 1 is 2*1+2 = 4

        Complexity:
            Time: O(log(n))
            Space: O(log(n)) for the recursion depth (tree height), or O(1) if using an iterative approach

        Insert
                  _5_
                /     \
               20     15
              / \    /  \
             22  40 25

        insert(2):
        Insert at the right-most spot to maintain the heap property.

                  _5_
                /     \
               20     15
              / \    /  \
             22  40 25   2

        Bubble up 2: Swap 2 and 15

                  _5_
                /     \
               20     2
              / \    / \
             22  40 25  15

        Bubble up 2: Swap 2 and 5

                  _2_
                /     \
               20     5
              / \    / \
             22  40 25  15
        We'll use an array to represent the tree, here are the indices:

                  _0_
                /     \
               1       2
              / \     / \
             3   4   5   6
        To get to a parent, we take (index - 1) // 2.
        For example, the parent of index 6 is (6 - 1) // 2 = 2.

        Complexity:
            Time: O(lg(n))
            Space: O(lg(n)) for the recursion depth (tree height), or O(1) if using an iterative approach

'''
# Solution

import sys

class MinHeapSolution:

    def __init__(self):
        self.array = []

    def __len__(self):
        return len(self.array)

    def extract_min(self):
        if not self.array:
            return None
        if len(self.array == 1):
            return self.array.pop(0)
        minimum = self.array[0]
        # Move the last element to the root
        self.array[0] = self.array.pop(-1)
        self._bubble_down(index = 0)
        return minimum

    def peek_min(self):
        return self.array[0] if self.array else None

    def insert(self, key):
        if key is None:
            raise TypeError('key cannot be None')
        self.array.append(key)
        self._bubble_up(index=len(self.array)-1)

    def _bubble_up(self, index):
        if index == 0:
            return
        index_parent = (index-1)//2
        if self.array[index] < self.array[index_parent]:
            # swap the indices and recurse
            self.array[index], self.array[index_parent] = self.array[index_parent], self.array[index]
            self._bubble_up(index_parent)

    def _bubble_down(self, index):
        min_child_index  = self._find_smaller_child(index)
        if min_child_index == -1:
            return
        if self.array[index] > self.array[min_child_index]:
            # Swap the indices and recurse
            self.array[index], self.array[min_child_index] = self.array[min_child_index], self.array[index]
            self._bubble_down(min_child_index)

    def _find_smaller_child(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        # No right child
        if right_child_index >= len(self.array):
            # No left child
            if left_child_index >= len(self.array):
                return -1
            # Left child only
            else:
                return left_child_index
        else:
            # Compare left and right children
            if self.array[left_child_index] < self.array[right_child_index]:
                return left_child_index
            else:
                return right_child_index
