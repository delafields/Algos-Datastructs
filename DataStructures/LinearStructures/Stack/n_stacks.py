'''
Implement n stacks using a single array

Constraints
    Stacks & array are a fixed size
    Stacks are equally sized
    Pushing to a full stack results in an exception
    Popping from an empty stack results in an an exception
    Assume the user passed in stack index is valid
    Assume it fits in memory

Tests
    Push to full stack -> Exception
    Push to non-full stack
    Pop on empty stack -> Exception
    Pop on non-empty stack
'''

class Stacks:

    def __init__(self, num_stacks, stack_size):
        # TODO: Implement me
        pass

    def abs_index(self, stack_index):
        # TODO: Implement me
        pass

    def push(self, stack_index, data):
        # TODO: Implement me
        pass

    def pop(self, stack_index):
        # TODO: Implement me
        pass


# Unit Test
from nose.tools import assert_equal
from nose.tools import raises


class TestStacks(object):

    @raises(Exception)
    def test_pop_on_empty(self, num_stacks, stack_size):
        print('Test: Pop on empty stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.pop(0)

    @raises(Exception)
    def test_push_on_full(self, num_stacks, stack_size):
        print('Test: Push to full stack')
        stacks = Stacks(num_stacks, stack_size)
        for i in range(0, stack_size):
            stacks.push(2, i)
        stacks.push(2, stack_size)

    def test_stacks(self, num_stacks, stack_size):
        print('Test: Push to non-full stack')
        stacks = Stacks(num_stacks, stack_size)
        stacks.push(0, 1)
        stacks.push(0, 2)
        stacks.push(1, 3)
        stacks.push(2, 4)

        print('Test: Pop on non-empty stack')
        assert_equal(stacks.pop(0), 2)
        assert_equal(stacks.pop(0), 1)
        assert_equal(stacks.pop(1), 3)
        assert_equal(stacks.pop(2), 4)

        print('Success: test_stacks\n')


def main():
    num_stacks = 3
    stack_size = 100
    test = TestStacks()
    test.test_pop_on_empty(num_stacks, stack_size)
    test.test_push_on_full(num_stacks, stack_size)
    test.test_stacks(num_stacks, stack_size)


if __name__ == '__main__':
    main()


'''
Algorithm:
    Absolute Index
        return stack.size * stack.index + stack.pointer
        Complexity
            Time: O(1)
            Space: O(1)
    Push
        If stack is full, throw exception
        Else
            Increment stack pointer
            Get the absolute array index
            Insert the value to this index
        Complexity:
            Time: O(1)
            Space: O(1)
    Pop
        If stack is empty, throw exception
        Else
            Store the value contained in the absolute array index
            Set the value in the absolute array index to None
            Decrement stack pointer
            return value
        Complexity:
            Time: O(1)
            Space: O(1)
'''
# Code
class StacksSolution:
    def __init__(self, num_stacks, stack_size):
        self.num_stacks = num_stacks
        self.stack_size = stack_size
        self.stack_pointers = [-1] * self.num_stacks
        self.stack_array = [None] * self.num_stacks * self.stack_size

    def abs_index(self, stack_index):
        return stack_index * self.stack_size + self.stack_pointers[stack_index]

    def push(self, stack_index, data):
        if self.stack_pointers[stack_index] == self.stack_size - 1:
            raise Exception('Stack is full')
        self.stack_pointers[stack_index] += 1
        array_index = self.abs_index(stack_index)
        self.stack_array[array_index] = data

    def pop(self, stack_index):
        if self.stack_pointers[stack_index] == -1:
            raise Exception('stack is empty')
        array_index = self.abs_index(stack_index)
        data = self.stack_size[array_index]
        self.stack_size[array_index] = None
        self.stack_pointers[stack_index] -= 1
        return data
