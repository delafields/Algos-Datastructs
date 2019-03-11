'''
Check if a binary tree is balanced

Constraints
    A balanced tree is where the height of two subtrees
        of any node doesn't differ more than one
    Raise an exception on a None input
    Assume we have a Node class with an insert method
    Assume it fits in memory

Test Cases
    None -> No
    1 -> Yes
    5, 3, 8, 1, 4 -> Yes
    5, 3, 8, 9, 10 -> No
'''

# Implement
class BstBalance(Bst):

    def check_balance(self):
        # TODO: Implement me
        pass


# Unit Tests

from nose.tools import assert_equal
from nose.tools import raises


class TestCheckBalance(object):

    @raises(TypeError)
    def test_check_balance_empty(self):
        bst = BstBalance(None)
        bst.check_balance()

    def test_check_balance(self):
        bst = BstBalance(Node(5))
        assert_equal(bst.check_balance(), True)

        bst.insert(3)
        bst.insert(8)
        bst.insert(1)
        bst.insert(4)
        assert_equal(bst.check_balance(), True)

        bst = BstBalance(Node(5))
        bst.insert(3)
        bst.insert(8)
        bst.insert(9)
        bst.insert(10)
        assert_equal(bst.check_balance(), False)

        bst = BstBalance(Node(3))
        bst.insert(2)
        bst.insert(1)
        bst.insert(5)
        bst.insert(4)
        bst.insert(6)
        bst.insert(7)
        assert_equal(bst.check_balance(), True)

        print('Success: test_check_balance')


def main():
    test = TestCheckBalance()
    test.test_check_balance_empty()
    test.test_check_balance()

'''
Algorithm
    We can check whether the tree is balanced while checking for heights

    Base Case: If the root is None
        return None
    Recursively check whether the left subtree is balanced and get its height 'left_height'
    Recursively check whether the right subtree is balanced and get its height 'right_height'
    Compare the left_height and right_height
    Return 1 + max(left_height + right_height)

    Complexity:
        Time: O(n)
        Space: O(h) where h is the height of the tree
'''

# Solution

class BstBalanceSolution(Bst):

    def _check_balance(self, node):
        if node is None:
            return 0
        left_height = self._check_balance(node.left)
        if left_height == -1:
            return -1
        right_height = self._check_balance(node.right)
        if right_height == -1:
            return -1
        diff = abs(left_height - right_height)
        if diff > 1:
            return -1
        return 1 + max(left_height, right_height)

    def check_balance(self):
        if self.root is None:
            return TypeError('root cannot be None')
        height = self._check_balance(self.root)
        return height != -1
