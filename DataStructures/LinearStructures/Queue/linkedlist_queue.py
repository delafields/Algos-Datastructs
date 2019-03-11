'''
Implement a queue with dequeue and enqueue using a linked list

Constraints
    If there is one item in the list
        Expect the head and tail pointers to both point to it
    If there are no items in the list
        Expect the head and tail pointers to be None
    If you dequeue of an empty queue, return None
    Assume it fits in memory

Tests
    Enqueue to an empty queue
    Enqueue to a non-empty queue
    Dequeue to an empty queue -> None
    Dequeue a queue with one element
    Dequeue a queue with more than one element
'''
# Implement
class Node(object):

    def __init__(self, data):
        # TODO: Implement me
        pass


class Queue(object):

    def __init__(self):
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


class TestQueue(object):

    # TODO: It would be better if we had unit tests for each
    # method in addition to the following end-to-end test
    def test_end_to_end(self):
        print('Test: Dequeue an empty queue')
        queue = Queue()
        assert_equal(queue.dequeue(), None)

        print('Test: Enqueue to an empty queue')
        queue.enqueue(1)

        print('Test: Dequeue a queue with one element')
        assert_equal(queue.dequeue(), 1)

        print('Test: Enqueue to a non-empty queue')
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)

        print('Test: Dequeue a queue with more than one element')
        assert_equal(queue.dequeue(), 2)
        assert_equal(queue.dequeue(), 3)
        assert_equal(queue.dequeue(), 4)

        print('Success: test_end_to_end')


def main():
    test = TestQueue()
    test.test_end_to_end()


if __name__ == '__main__':
    main()

# Solution
'''
Algorithm
    Enqueue
        If the list is empty
            Set head and tail to None
        Else
            Set tail to node

        Complexity:
            Time: O(1)
            Space: O(1)

    Dequeue
        If the list is empty:
            return None
        If the list has one node
            save the head node's value
            Set head and tail to None
            return the saved node
        Else
            Save the head node's value
            Set head to its next node
            Return the saved node

        Complexity:
            Time: O(1)
            Space: O(1)
'''

class NodeSolution:

    def __init__(self, data):
        self.data = data
        self.next = None

class QueueSolution:

    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self, data):
        node = NodeSolution(data)
        # Empty List
        if self.head is None and self.tail is None:
            self.head = node
            self.tail = node
        else:
            self.tail.next = node
            self.tail = node

    def dequeue(self):
        # Empty List
        if self.head is None and self.tail is None:
            return None
        data = self.head.data
        # Remove only element from a one element list
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
        return data
