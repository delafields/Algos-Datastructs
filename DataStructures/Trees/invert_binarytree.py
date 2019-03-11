'''
Invert a binary tree

Constraints
    Invert means to swap all left and right node pairs
    Assume we already have a Node class
    Do not assume inputs are valid
    Assume it fits in memory

Test Cases
    Input:
             5
           /   \
          2     7
         / \   / \
        1   3 6   9

    Output:
             5
           /   \
          7     2
         / \   / \
        9   6 3   1
'''

# Implement
class InverseBst(Bst):

    def invert_tree(self):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestInvertTree(object):

    def test_invert_tree(self):
        root = Node(5)
        bst = InverseBst(root)
        node2 = bst.insert(2)
        node3 = bst.insert(3)
        node1 = bst.insert(1)
        node7 = bst.insert(7)
        node6 = bst.insert(6)
        node9 = bst.insert(9)
        result = bst.invert_tree()
        assert_equal(result, root)
        assert_equal(result.left, node7)
        assert_equal(result.right, node2)
        assert_equal(result.left.left, node9)
        assert_equal(result.left.right, node6)
        assert_equal(result.right.left, node3)
        assert_equal(result.right.right, node1)
        print('Success: test_invert_tree')


def main():
    test = TestInvertTree()
    test.test_invert_tree()


if __name__ == '__main__':
    main()

'''
Algorithm
    Base Case: If the root is None, return
    Recursive Case:
        Recurse on the left node
        Recurse on the right node
        Swap left and right
    Return the node

    Complexity:
        Time: O(n)
        Space: O(h), where h is the height, for the recursion depth
'''

# Solution

class InverseBstSolution(Bst):

    def invert_tree(self):
        if self.root is None:
            return TypeError('root cannot be None')
        return self._inver_tre(self.root)

    def _invert_tree(self, root):
        if root is None:
            return
        self._invert_tree(root.left)
        self._invert_tree(root.right)
        root.left, root.right = root.right, root.left
        return root
