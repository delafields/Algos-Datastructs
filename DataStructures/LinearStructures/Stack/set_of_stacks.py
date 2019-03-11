'''
Implement SetOfStacks that wraps a list of stacks, where each stack is bound by a capacity

Constraints
    We can assume we already have a Stack class
    All stacks are bound by the same capacity
    If a stack becomes full, we automatically create another
    If a stack becomes empty, we delete it
    If we pop on an empty stack, we return None
    We assume this fits in memory

Tests
    Push and pop on an empty stack
    Push and pop on a non-empty stack
    Push on a capacity Stack to create a new one
    Pop on a stack to destroy it
'''
# Implement
class StackWithCapacity(Stack):

    def __init__(self, top=None, capacity=10):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass

    def is_full(self):
        # TODO: Implement me
        pass


class SetOfStacks(object):

    def __init__(self, indiv_stack_capacity):
        # TODO: Implement me
        pass

    def push(self, data):
        # TODO: Implement me
        pass

    def pop(self):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestSetOfStacks(object):

    def test_set_of_stacks(self):
        print('Test: Push on an empty stack')
        stacks = SetOfStacks(indiv_stack_capacity=2)
        stacks.push(3)

        print('Test: Push on a non-empty stack')
        stacks.push(5)

        print('Test: Push on a capacity stack to create a new one')
        stacks.push('a')

        print('Test: Pop on a stack to destroy it')
        assert_equal(stacks.pop(), 'a')

        print('Test: Pop general case')
        assert_equal(stacks.pop(), 5)
        assert_equal(stacks.pop(), 3)

        print('Test: Pop on no elements')
        assert_equal(stacks.pop(), None)

        print('Success: test_set_of_stacks')


def main():
    test = TestSetOfStacks()
    test.test_set_of_stacks()


if __name__ == '__main__':
    main()

# Solution
'''
Algorithm

    Push
        If there are no stacks or the last stack is full
            Create a new stack
        Push to the new stack

        Complexity:
            Time: O(1)
            Space: O(m), where m is the size of the new stack if the last stack is full

    Pop
        If there are no stacks
            return None
        Else if the last stack has one element
            Pop the last element's data
            Delete the now empty stack
            Update the last stack pointer
        Else
            Pop the last element's data
        Return the last element's data

        Complexity:
            Time: O(1)
            Space: O(1)
'''
class StackWithCapacitySolution(Stack):

    def __init__(self, top=None, capacity=10):
        super(StackWithCapacitySolution, self).__init__(top)
        self.capacity = capacity
        self.num_items = 0

    def push(self, data):
        if self.is_full():
            raise Exception('Stack is full')
        super(StackWithCapacitySolution, self).push(data)
        self.num_items += 1

    def pop(self):
        self.num_items -= 1
        return super(StackWithCapacitySolution, self).pop()

    def is_full(self):
        return self.num_items == self.capacity

    def is_empty(self):
        return self.num_items == 0

class SetOfStacksSolution:

    def __init__(self, indiv_stack_capacity):
        self.indiv_stack_capacity = indiv_stack_capacity
        self.stacks = []
        self.last_stack = None

    def push(self, data):
        if self.last_stack is None or self.last_stack.is_full():
            self.last_stack = StackWithCapacitySolution(None, self.indiv_stack_capacity)
            self.stacks.append(self.last_stack)
        self.last_stack.push(data)

    def pop(self):
        if self.last_stack is None:
            return None
        data = self.last_stack.pop()
        if self.last_stack.pop()
        if self.last_stack.is_empty():
            self.stacks.pop()
            self.last_stack = self.stacks[-1] if self.stacks else None
        return data
