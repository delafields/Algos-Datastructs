'''
Implement depth-first traversals (in-order, pre-order, post-order) on a binary tree

Constraints
    Assume we have a node class with an insert method
    Call visit_func on each node we process
    Assume it fits in memory

Test Cases
    In-Order Traversal
        5, 2, 8, 1, 3 -> 1, 2, 3, 5, 8
        1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
    Pre-Order Traversal
        5, 2, 8, 1, 3 -> 5, 2, 1, 3, 8
        1, 2, 3, 4, 5 -> 1, 2, 3, 4, 5
    Post-Order Traversal
        5, 2, 8, 1, 3 -> 1, 3, 2, 8, 5
        1, 2, 3, 4, 5 -> 5, 4, 3, 2, 1
'''

# Implement

class BstDfs(Bst):

    def in_order_traversal(self, node, visit_func):
    # TODO: Implement me
    pass

    def pre_order_traversal(self, node, visit_func):
        # TODO: Implement me
        pass

    def post_order_traversal(self,node, visit_func):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestDfs(object):

    def __init__(self):
        self.results = Results()

    def test_dfs(self):
        bst = BstDfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)

        bst.in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 5, 8]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[5, 2, 1, 3, 8]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 3, 2, 8, 5]")
        self.results.clear_results()

        bst = BstDfs(Node(1))
        bst.insert(2)
        bst.insert(3)
        bst.insert(4)
        bst.insert(5)

        bst.in_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.pre_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[1, 2, 3, 4, 5]")
        self.results.clear_results()

        bst.post_order_traversal(bst.root, self.results.add_result)
        assert_equal(str(self.results), "[5, 4, 3, 2, 1]")

        print('Success: test_dfs')


def main():
    test = TestDfs()
    test.test_dfs()


if __name__ == '__main__':
    main()


'''
Algorithm
    Inorder
        Recursively call inorder on the left child
        Visit the current node
        Recursively call inorder on the right child

        Complexity:
            Time: O(n)
            Space: O(m), where m is the recursion depth, or O(1) for an iterative approach

    Preorder
        Visit the current node
        Recursively call preorder on the left child
        Recursively call preorder on the right child

        Complexity:
            Time: O(n)
            Space: O(m), where m is the recursion depth, or O(1) for an iterative approach

    Postorder
        Recursively call postorder on the left child
        Recursively call postorder on the right child
        Visit the current node

        Complexity:
            Time: O(n)
            Space: O(m), where m is the recursion depth, or O(1) for an iterative approach
'''

# Solution

class BstDfsSolution(Bst):

    def in_order_traversal(self, node, visit_func):
        if node is not None:
            self.in_order_traversal(node.left, visit_func)
            visit_func(node)
            self.in_order_traversal(node.right, visit_func)

    def pre_order_traversal(self, node, visit_func):
        if node is not None:
            visit_func(node)
            self.pre_order_traversal(node.left, visit_func)
            self.pre_order_traversal(node.right, visit_func)

    def post_order_traversal(self,node, visit_func):
        if node is not None:
            self.post_order_traversal(node.left, visit_func)
            self.post_order_traversal(node.right, visit_func)
            visit_func(node)
