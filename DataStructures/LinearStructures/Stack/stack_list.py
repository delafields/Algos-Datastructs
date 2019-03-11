'''
Implement a stack with push, pop, peek, and is_empty using a linked list

Constraints
    If we pop an empty stack it returns None
    We assume it fits in memory

Tests
    Push to an empty stack
    Push to a non-empty stack
    Pop on an empty stack
    Pop on a non-empty stack
    Pop on a multiple element stack
    Peek on an empty stack
    Peek on a non-empty stack
    Is empty on an empty stack
    Is empty on a non-empty stack
'''
# Implement
class Node(object):

    def __init__(self, data):
        # TODO: Implement me
        pass


class Stack(object):

    def __init__(self, top=None):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass

    def peek(self):
        # TODO: Implement me
        pass

    def is_empty(self):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestStack(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Empty stack')
        stack = Stack()
        assert_equal(stack.peek(), None)
        assert_equal(stack.pop(), None)

        print('Test: One element')
        top = Node(5)
        stack = Stack(top)
        assert_equal(stack.pop(), 5)
        assert_equal(stack.peek(), None)

        print('Test: More than one element')
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        assert_equal(stack.pop(), 3)
        assert_equal(stack.peek(), 2)
        assert_equal(stack.pop(), 2)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.is_empty(), False)
        assert_equal(stack.pop(), 1)
        assert_equal(stack.peek(), None)
        assert_equal(stack.is_empty(), True)

        print('Success: test_end_to_end')


def main():
    test = TestStack()
    test.test_end_to_end()


if __name__ == '__main__':
    main()

'''
Algorithm
    Push
        Create new node with value
        Set node's next to top
        Set top to node

        Complexity:
            Time: O(1)
            Space: O(1)

    Pop
        If stack is empty, return None
        Else
            Save top's value
            Set top to top.next
            Return saved value

        Complexity:
            Time: O(1)
            Space: O(1)

    Peek
        If stack is empty return None
        Else return top's value

        Complexity:
            Time: O(1)
            Space: O(1)

    Is Empty
        If peek has a value return False
        Else return True

        Complexity:
            Time: O(1)
            Space: O(1)

'''
# Solution
class NodeSolution:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class StackSolution:

    def __init__(self, top=None):
        self.top = top

    def push(self, data):
        self.top = Node(data, self.top)

    def pop(self):
        if self.top = None:
            return None
        data = self.top.data
        self.top = self.top.next
        return data

    def peek(self):
        return self.top.data if self.top is not None else None

    def is_empty(self):
        return self.peek() is None
