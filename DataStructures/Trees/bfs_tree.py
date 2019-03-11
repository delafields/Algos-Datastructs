'''
Implement breadth-first traversal on a binary tree

Constraints
    We can assume we have a Node class with an insert method
    We can assume it fits in memory
    When you process a node, call an input method visit_func on it

Test Cases
    5, 2, 8, 1, 3 -> 5, 2, 8, 1, 3
'''

# Implement

class BstBfs(Bst):

    def bfs(self, visit_func):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestBfs(object):

    def __init__(self):
        self.results = Results()

    def test_bfs(self):
        bst = BstBfs(Node(5))
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        bst.bfs(self.results.add_result)
        assert_equal(str(self.results), '[5, 2, 8, 1, 3]')

        print('Success: test_bfs')


def main():
    test = TestBfs()
    test.test_bfs()


if __name__ == '__main__':
    main()


'''
Algorithm
    Initialize queue with root
    While queue is not empty
        Deque and print the node
        Queue the left child
        Queue the right child

    Complexity:
        Time: O(n)
        Space: O(n), extra space for the queue
'''

# Solution

from collections import deque

class BstBfsSolution(Bst):

    def bfs(self, visit_func):
        if self.root is None:
            raise TypeError('root cannot be None')
        queue = deque()
        queue.append(self.root)
        while queue:
            node = queue.popleft()
            if node.left is not None:
                queue.append(node.left)
            if node.right is not None:
                queue.append(node.right)
