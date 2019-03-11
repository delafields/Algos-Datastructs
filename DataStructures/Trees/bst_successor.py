'''
Find the in-order successor of a given node in a bst

Constraints
    If the successor is None return None
    If the input is None, throw an exception
    Assume we have a Node class that tracks parents
    Assume it fits in memory

Test Cases
          _5_
        /     \
       3       8
      / \    /   \
     2   4  6    12
    /        \   / \
   1          7 10  15
               /
              9

In: None  Out: Exception
In: 4     Out: 5
In: 5     Out: 6
In: 8     Out: 9
In: 15    Out: None
'''

# Implement
class BstSuccessor:

    def get_next(self, node):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal
from nose.tools import raises


class TestBstSuccessor(object):

    @raises(Exception)
    def test_bst_successor_empty(self):
        bst_successor = BstSuccessor()
        bst_successor.get_next(None)

    def test_bst_successor(self):
        nodes = {}
        node = Node(5)
        nodes[5] = node
        bst = Bst(nodes[5])
        nodes[3] = bst.insert(3)
        nodes[8] = bst.insert(8)
        nodes[2] = bst.insert(2)
        nodes[4] = bst.insert(4)
        nodes[6] = bst.insert(6)
        nodes[12] = bst.insert(12)
        nodes[1] = bst.insert(1)
        nodes[7] = bst.insert(7)
        nodes[10] = bst.insert(10)
        nodes[15] = bst.insert(15)
        nodes[9] = bst.insert(9)

        bst_successor = BstSuccessor()
        assert_equal(bst_successor.get_next(nodes[4]), 5)
        assert_equal(bst_successor.get_next(nodes[5]), 6)
        assert_equal(bst_successor.get_next(nodes[8]), 9)
        assert_equal(bst_successor.get_next(nodes[15]), None)

        print('Success: test_bst_successor')


def main():
    test = TestBstSuccessor()
    test.test_bst_successor()
    test.test_bst_successor_empty()


if __name__ == '__main__':
    main()


'''
Algorithm
    If the node has a right subtree
        Return the left-most node in the right subtree
    Else
        Go up until you find a node that is its parent's left node
            If you get to the root (node.parent is None)
                Return None
                (The original input must be the largest in the tree)
            Else
                Return the parent

    Complexity:
        Time: O(h), where h is the height of the tree
        Space: O(h), where h is the recursion depth (tree height), or O(1) if using an iterative approach
'''

# Solution

class BstSuccessorSolution:

    def get_next(self, node):
        if node is None:
            raise TypeError('node cannot be None')
        if node.right is not None:
            return self._left_most(node.right)
        else:
            return self._next_ancestor(node)

    def _left_most(self, node):
        if node.left is not None:
            return self._left_most(node.left)
        else:
            return node.data

    def _next_ancestor(self, node):
        if node.parent is not None:
            if node.parent.data > node.data:
                return node.parent.data
            else:
                return self._next_ancestor(node.parent)
        # We reached the root, the original input node
        # must be the largest element in the tree
        return None
