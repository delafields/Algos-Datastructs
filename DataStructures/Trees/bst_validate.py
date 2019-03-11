'''
Determine if a tree is a valid binary search tree

Constraints
    The tree CAN have duplicates
    If this is called on a None input, raise an exception
    Assume we already have a Node class
    Assume it fits in memory

Test Cases
    Valid:
          5
        /   \
       5     8
      /     /
     4     6
            \
             7

    Invalid:
          5
        /   \
       5     8
      / \   /
     4   9 7
'''

# Implement

class BstValidate(Bst):

    def validate(self):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal
from nose.tools import raises


class TestBstValidate(object):

    @raises(Exception)
    def test_bst_validate_empty(self):
        validate_bst(None)

    def test_bst_validate(self):
        bst = BstValidate(Node(5))
        bst.insert(8)
        bst.insert(5)
        bst.insert(6)
        bst.insert(4)
        bst.insert(7)
        assert_equal(bst.validate(), True)

        bst = BstValidate(Node(5))
        left = Node(5)
        right = Node(8)
        invalid = Node(20)
        bst.root.left = left
        bst.root.right = right
        bst.root.left.right = invalid
        assert_equal(bst.validate(), False)

        print('Success: test_bst_validate')


def main():
    test = TestBstValidate()
    test.test_bst_validate_empty()
    test.test_bst_validate()


if __name__ == '__main__':
    main()

'''
Algorithm
    We'll use a recursive solution that validates left <= current < right
    passing down the min and max values as we do a Depth-First Traversak

    If the node is None
        Return True
    If min is set and node's value <= min
        return False
    If max is set and the node's value > max
        return False
    Recursively call the validate function on the node.left, updating max
    Recursively call the validate function on the node.right, updating min

    Complexity:
        Time: O(n)
        Space: O(h) where h is the height of the tree
'''

# Solution

import sys

class BstValidateSolution(Bst):

    def validate(self):
        if self.root is None:
            raise TypeError('No root node')
        return self._validate(self.root)

    def _validate(self, node, min=-sys.maxsize, max=sys.maxsize):
        if node is None:
            return True
        if node.data <= min or node.data > max:
            return False
        if not self._validate(node.left, min, node.data):
            return False
        if not self._validate(node.right, node.data, max):
            return False
        return True
