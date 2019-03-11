'''
Implement a Queue using 2 Stacks

Constraints
    We expect the methods to be enqueue and dequeue
    We can assume we already have a stack class
    We cannot push a None value to the Stack
    We can assume this fits in memory

Tests
    Enqueue and dequeue on empty stack
    Enqueue and dequeue on non-empty stack
    Multiple enqueue in a row
    Multiple dequeue in a row
    Enqueue after a dequeue
    Dequeue after an enqueue
'''
# Implement
class QueueFromStacks(object):

    def __init__(self):
        # TODO: Implement me
        pass

    def shift_stacks(self, source, destination):
        # TODO: Implement me
        pass

    def enqueue(self, data):
        # TODO: Implement me
        pass

    def dequeue(self):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestQueueFromStacks(object):

    def test_queue_from_stacks(self):
        print('Test: Dequeue on empty stack')
        queue = QueueFromStacks()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue on empty stack')
        print('Test: Enqueue on non-empty stack')
        print('Test: Multiple enqueue in a row')
        num_items = 3
        for i in range(0, num_items):
            queue.enqueue(i)

        print('Test: Dequeue on non-empty stack')
        print('Test: Dequeue after an enqueue')
        assert_equal(queue.dequeue(), 0)

        print('Test: Multiple dequeue in a row')
        assert_equal(queue.dequeue(), 1)
        assert_equal(queue.dequeue(), 2)

        print('Test: Enqueue after a dequeue')
        queue.enqueue(5)
        assert_equal(queue.dequeue(), 5)

        print('Success: test_queue_from_stacks')


def main():
    test = TestQueueFromStacks()
    test.test_queue_from_stacks()


if __name__ == '__main__':
    main()

'''
Algorithm
    We'll use two stacks (left and right) to implement the queue
        The left stack will be used for enqueue
        The right stack will be used for dequeue
    To prevent multiple dequeue calls from needlessly shifting elements around between the stacks, we'll shift elements lazily.

    Enqueue
        If right stack is not empty
            Shift the elements of the right stack to the left stack
        Push the data to the left Stack

        Complexity:
            Time: O(n)
            Space: O(n)

    Dequeue
        If the left stack is not empty
            Shift the elements of the left stack to the right stack
        Pop from the right stack and return the data

        Complexity:
            Time: O(n)
            Space: O(n)

    Shift Stacks
        While the source stack has elements
            Pop from the source stack and push the data onto the destination stack

        Complexity:
            Time: O(n)
            Space: O(1)
'''
class QueueFromStacksSolution:

    def __init__(self):
        self.left_stack = Stack()
        self.right_stack = Stack()

    def shift_stacks(self, source, destination):
        while source.peek() is not None:
            destination.push(source.pop())

    def enqueue(self, data):
        self.shift_stacks(self.right_stack, self.left_stack)
        self.left_stack.push(data)

    def dequeue(self):
        self.shift_stacks(self.left_stack, self.right_stack)
        return self.right_stack.pop()


####################################
class TwoStackQueueNonShifting(self):

    def __init__(self):
        self.instack = []
        self.outstack = []

    def enqueue(self, element):
        self.instack.append(element)

    def dequeue(self):
        if not self.outstack:
            while self.instack:
                self.outstack.append(self.instack.pop())

        return self.outstack.pop()

'''
The key insight is that a stack reverses order (while a queue doesn't)
A sequence of elements pushed on a stack comes back in reversed order when popped.
Consquently, two stacks chained together will return elements in the same order, since reversed order reversed again is original order

We use an in-stack that we fill when an element in enqueued and the dequeue operation takes elements from an out-stack
If the out-stack is empty, we pop all elements from the in-stack and push them onto the out-stack
'''
