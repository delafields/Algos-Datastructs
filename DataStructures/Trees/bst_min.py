'''
Create a binary search tree with minimal height from a sorted array

Constraints
    The array is in increasing order
    Each element is unique
    We can assume we already have a node class
    Assume it fits in memory

Test Cases
    0, 1, 2, 3, 4, 5, 6 -> height 3
    0, 1, 2, 3, 4, 5, 6, 7 -> height 4
'''
# Implement

class MinBst:

    def create_min_bst(self, array):
        # TODO: Implement me

# Test Cases
from nose.tools import assert_equal


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left),
                   height(node.right))


class TestBstMin(object):

    def test_bst_min(self):
        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6]
        root = min_bst.create_min_bst(array)
        assert_equal(height(root), 3)

        min_bst = MinBst()
        array = [0, 1, 2, 3, 4, 5, 6, 7]
        root = min_bst.create_min_bst(array)
        assert_equal(height(root), 4)

        print('Success: test_bst_min')


def main():
    test = TestBstMin()
    test.test_bst_min()


if __name__ == '__main__':
    main()

'''
Algorithm
    To create a bst with minimum height, we need to use the middle element as the root.
    We'll use recursion to divide the array in half and continue to pick the middle element
    from the left and right halves as nodes to insert in the tree

    create_min_bst(array, start, end)
    Base case: Stop when end < start
    Create a node with the mid element
    Recursively build node.left by calling create_min_bst using the left sub array
    Recursively build node.right by calling create_min_bst using the right sub array
    Return the node

    Complexity:
        Time: O(n)
        Space: O(h), where h is the tree's height (since this is a tree with min height, h = log h)
'''

# Solution

class MinBstSolution:

    def create_min_bst(self, array):
        if array is None:
            return
        return self._create_min_bst(array, 0, len(array)-1)

    def _create_min_bst(self, array, start, end):
        if end < start:
            return None

        mid = (start+end)//2
        node = Node.data(array[mid])
        node.left = self._create_min_bst(array, start, mid-1)
        node.right = self._create_min_bst(array, mid+1, end)
        return node
