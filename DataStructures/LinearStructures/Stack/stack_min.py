'''
Implement a stack with push, pop, and min methods running O(1) time
'''
'''
Constraints
    Assume it is a stack of ints
    Assume the input values for push are valid
    If we call this on an empty stack, we return sys.maxsize
    Assume we have a stack class that can be used for this problem
    Assume it fits in memory

Tests
    Push/pop on an empty stack
    Push/pop on a non-empty stack
    Min on an empty stack
    Min on a non-empty stack
'''
import sys
from Stack import Stack


class StackMin(Stack):

    def __init__(self, top=None):
        # TODO: Implement me
        pass

    def minimum(self):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass

# Unit Test
from nose.tools import assert_equal


class TestStackMin(object):

    def test_stack_min(self):
        print('Test: Push on empty stack, non-empty stack')
        stack = StackMin()
        stack.push(5)
        assert_equal(stack.peek(), 5)
        assert_equal(stack.minimum(), 5)
        stack.push(1)
        assert_equal(stack.peek(), 1)
        assert_equal(stack.minimum(), 1)
        stack.push(3)
        assert_equal(stack.peek(), 3)
        assert_equal(stack.minimum(), 1)
        stack.push(0)
        assert_equal(stack.peek(), 0)
        assert_equal(stack.minimum(), 0)

        print('Test: Pop on non-empty stack')
        assert_equal(stack.pop(), 0)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 3)
        assert_equal(stack.minimum(), 1)
        assert_equal(stack.pop(), 1)
        assert_equal(stack.minimum(), 5)
        assert_equal(stack.pop(), 5)
        assert_equal(stack.minimum(), sys.maxsize)

        print('Test: Pop empty stack')
        assert_equal(stack.pop(), None)

        print('Success: test_stack_min')


def main():
    test = TestStackMin()
    test.test_stack_min()


if __name__ == '__main__':
    main()

'''
Algorithm
(We'll use a second stack to keep track of the min values)
    Min
        If the second stack is empty, return an error(max int value)
        Else, return the top of the stack, without popping it
        Complexity
            Time: O(1)
            Space: O(1)
    Push
        Push the data
        If the data is less than min, push data to second stack
        Complexity
            Time: O(1)
            Space: O(1)
    Pop
        Pop the data
        If the data is equal to min
            Pop the top of the second stack
        Return the data
        Complexity
            Time: O(1)
            Space: O(1)
'''

class StackMinSolution(Stack):

    def __init__(self, top=None):
        super(StackMinSolution, self).__init__(top)
        self.stack_of_mins = Stack()

    def minimum(self):
        if self.stack_of_mins.top is None:
            return sys.maxsize
        else:
            return self.stack_of_mins.peek()

    def push(self, data):
        super(StackMinSolution, self).push(data)
        if data < self.minimum():
            self.stack_of_mins.push(data)

    def pop(self):
        data = super(StackMinSolution, self).pop()
        if data == self.minimum():
            self.stack_of_mins.pop()
        return data
