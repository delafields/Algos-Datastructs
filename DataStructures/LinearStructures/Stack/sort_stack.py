'''
Sort a stack. You can use another stack as a buffer.

Constraints
    When sorted, the largest element should be at the top
    You can have duplicate values
    We can assume we already have a stack class
    We assume this fits in memory

Tests
    Empty stack -> None
    One element stack
    Two or more element stack (general case)
    Already sorted stack
'''
# Implement
class MyStack(Stack):

    def sort(self):
        # TODO: Implement me
        pass

# Unit Tests
from random import randint
from nose.tools import assert_equal


class TestSortStack(object):

    def get_sorted_stack(self, stack, numbers):
        for x in numbers:
            stack.push(x)
        sorted_stack = stack.sort()
        return sorted_stack

    def test_sort_stack(self, stack):
        print('Test: Empty stack')
        sorted_stack = self.get_sorted_stack(stack, [])
        assert_equal(sorted_stack.pop(), None)

        print('Test: One element stack')
        sorted_stack = self.get_sorted_stack(stack, [1])
        assert_equal(sorted_stack.pop(), 1)

        print('Test: Two or more element stack (general case)')
        num_items = 10
        numbers = [randint(0, 10) for x in range(num_items)]
        sorted_stack = self.get_sorted_stack(stack, numbers)
        sorted_numbers = []
        for _ in range(num_items):
            sorted_numbers.append(sorted_stack.pop())
        assert_equal(sorted_numbers, sorted(numbers, reverse=True))

        print('Success: test_sort_stack')


def main():
    test = TestSortStack()
    test.test_sort_stack(MyStack())
    try:
        test.test_sort_stack(MyStackSimplified())
    except NameError:
        # Alternate solutions are only defined
        # in the solutions file
        pass


if __name__ == '__main__':
    main()

# Solution
'''
Algorithm
    Our buffer will hold elements in reverse order, smallest at the top
    Store the current top element in a temp variable

    While stack is not empty:
        While buffer is not empty OR buffer top is > temp
            Move buffer top to stack
        Move temp to top of buffer
    return buffer

    Complexity:
        Time: O(n^2)
        Space: O(n)
'''
class MyStackSolution(Stack):

    def sort(self):
        buff = Stack()
        while not self.is_empty():
            temp = self.pop()
            while not buff.is_empty() and temp < buff.peek():
                self.push(buff.pop())
            buff.push(temp)
        return buff
