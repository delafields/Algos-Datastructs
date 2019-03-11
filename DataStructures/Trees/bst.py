'''
Implement a binary search tree with an insert method

Constraints
    Cannot insert None values
    Assume we are working with valid integers
    Assume all left descendents <= n < all right descendents
    Keep track of parent nodes
    Assume it fits in memory

Test Cases
    Insert (In-order done in the unit test)
        5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
        1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
'''
# Implement
class Node:

    def __init__(self, data):
        # TODO: Implement me
        pass


class Bst:

    def insert(self, data):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestTree(object):

    def __init__(self):
        self.results = Results()

    def test_tree_one(self):
        bst = Bst()
        bst.insert(5)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 5, 8]')
        self.results.clear_results()

    def test_tree_two(self):
        bst = Bst()
        bst.insert(1)
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)
        in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), '[1, 2, 3, 4, 5]')

        print('Success: test_tree')


def main():
    test = TestTree()
    test.test_tree_one()
    test.test_tree_two()


if __name__ == '__main__':
    main()

'''
Algorithm

    Insert
        If the root is None, return Node(data)
        If the data is <= the current node's data
            If the current node's left child is None, set it to Node(data)
            Else, recursively call insert on the left child
        Else
            If the current node's right child is None, set it to Node(data)
            Else, recursively call insert on the right child

    Complexity:
        Time: O(h), where h is the height of the tree
            In a balanced tree, the height is O(log n)
            In the worst case we have a linked list structure with O(n)
        Space: O(m), where m is the recursion depth, or O(1) if using an iterative approach
'''
# Solution

class NodeSolution:

    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None

    def __repr__(self):
        return str(self.data)

class BstSolution:

    def __init__(self, root=None):
        self.root = root

    def insert(self, data):
        if data is None:
            raise TypeError('data cannot be None')
        if self.root is None:
            self.root = Node(data)
            return self.root
        else:
            return self._insert(self.root, data)

    def _insert(self, node, data):
        if node is None:
            return Node(data)
        if data <= node.data:
            if node.left is None:
                node.left = self._insert(node.left, data)
                node.left.parent = node
                return node.left
            else:
                return self._insert(node.left, data)
    else:
        if node.right is None:
            node.right = self._insert(node.right, data)
            node.right.parent = node
            return node.right
        else:
            return self._insert(node.right, data)
