'''
Find the lowest common ancestor in a binary tree

Constraints
    This is not a binary search tree
    CANNOT assume the two nodes are in the tree
    Assume it fits in memory

Test Cases
         _10_
        /     \
       5       9
      / \     / \
     12  3   18  20
        / \      /
       1   8    40

    0, 5 -> None
    5, 0 -> None
    1, 8 -> 3
    12, 8 -> 5
    12, 40 -> 10
    9, 20 -> 9
    3, 5 -> 5
'''

# Implement
class Node:

    def __init__(self, key, left=None, right=None):
        self.key = key
        self.left = left
        self.right = right

    def __repr__(self):
        return str(self.key)

class BinaryTree:

    def lca(self, root, node1, node2):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestLowestCommonAncestor(object):

    def test_lca(self):
        node10 = Node(10)
        node5 = Node(5)
        node12 = Node(12)
        node3 = Node(3)
        node1 = Node(1)
        node8 = Node(8)
        node9 = Node(9)
        node18 = Node(18)
        node20 = Node(20)
        node40 = Node(40)
        node3.left = node1
        node3.right = node8
        node5.left = node12
        node5.right = node3
        node20.left = node40
        node9.left = node18
        node9.right = node20
        node10.left = node5
        node10.right = node9
        root = node10
        node0 = Node(0)
        binary_tree = BinaryTree()
        assert_equal(binary_tree.lca(root, node0, node5), None)
        assert_equal(binary_tree.lca(root, node5, node0), None)
        assert_equal(binary_tree.lca(root, node1, node8), node3)
        assert_equal(binary_tree.lca(root, node12, node8), node5)
        assert_equal(binary_tree.lca(root, node12, node40), node10)
        assert_equal(binary_tree.lca(root, node9, node20), node9)
        assert_equal(binary_tree.lca(root, node3, node5), node5)
        print('Success: test_lca')


def main():
    test = TestLowestCommonAncestor()
    test.test_lca()


if __name__ == '__main__':
    main()


'''
Algorithm
    Verify both nodes are in the tree
    Base Cases
        If the root is None
            return None
        If the root is either node
            return the root
    Recursively search left and right
    If the left and right are both nodes
        return the root
    Else
        left or right, whichever is valid

    Complexity:
        Time: O(h), where h is the height of the tree
        Space: O(h), where h is the recursion depth
'''
# Solution

class BinaryTreeSolution:

    def lca(self, root, node1, node2):
        if None in (root, node1, node2):
            return None
        if (not self._node_in_tree(root, node1)) or (not self._node_in_tree(root, node2)):
            return None
        self._lca(root, node1, node2)

    def _node_in_tree(self, root, node):
        if root is None:
            return False
        if root is node:
            return True
        left = self._node_in_tree(root.left, node)
        right = self._node_in_tree(root.right, node)
        return left or right

    def _lca(self, root, node1, node2):
        if root is None:
            return None
        if root is node1 or root is node2:
            return root
        left_node = self._lca(root.left, node1, node2)
        right_node = self._lca(root.right, node1, node2)
        if left_node is not None and right_node is not None:
            return root
    else:
        return left_node if left_node is not None else right_node

# ???
class LcaResult:

    def __init__(self, node, is_ancestor):
        self.node = node
        self.is_ancestor = is_ancestor


class BinaryTreeOptimized:

    def lca(self, root, node1, node2):
        if root is None:
            raise TypeError('root cannot be None')
        result = self._lca(root, node1, node2)
        if result.is_ancestor:
            return result.node
        return None

    def _lca(self, curr_node, node1, node2):
        if curr_node is None:
            return LcaResult(None, is_ancestor=False)
        if curr_node is node1 and curr_node is node2:
            return LcaResult(curr_node, is_ancestor=True)
        left_result = self._lca(curr_node.left, node1, node2)
        if left_result.is_ancestor:
            return left_result
        right_result = self._lca(curr_node.right, node1, node2)
        if right_result.is_ancestor:
            return right_result
        if left_result.node is not None and right_result.node is not None:
            return LcaResult(curr_node, is_ancestor=True)
        elif curr_node is node1 or curr_node is node2:
            is_ancestor = left_result.node is not None or \
                right_result.node is not None
            return LcaResult(curr_node, is_ancestor)
        else:
            return LcaResult(left_result.node if left_result.node is not None \
                                 else right_result.node, is_ancestor=False)
