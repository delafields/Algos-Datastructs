'''
Determine the height of a tree

Constraints
    This is a binary tree
    Assume we already have a Node class with an insert method
    Assume this fits in memory

Test Cases
    5 -> 1
    5, 2, 8, 1, 3 -> 3
'''

# Implement
class BstHeight(Bst):

    def height(self, node):
        # TODO: Implement Me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestHeight(object):

    def test_height(self):
        bst = BstHeight(Node(5))
        assert_equal(bst.height(bst.root), 1)
        bst.insert(2)
        bst.insert(8)
        bst.insert(1)
        bst.insert(3)
        assert_equal(bst.height(bst.root), 3)

        print('Success: test_height')


def main():
    test = TestHeight()
    test.test_height()


if __name__ == '__main__':
    main()

'''
Algorithm
    We'll use a recursive algorithm
        If the current node is None:
            Return 0
        Else:
            Return 1 + the max height of the left or right children

    Complexity:
        Time: O(n)
        Space: O(h) where h is the height of the tree
'''

# Solution

class BstHeightSolution(Bst):

    def height(self, node):
        if node is None:
            return 0
        return 1 + max(self.height(node.left),
                       self.height(node.right))
