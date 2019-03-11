'''
Find the start of a linked list loop

Constraints
    We can assume this is a single linked list
    We are not always passed a circular linked list
    When we find a loop, we return the node (not its data)
    We can assume we already have a linked list class

Test Cases
    Empty list -> None
    Not a circular list -> None
        One element
        Two or more elements
    Circular linked list general case
'''
# Implement
class MyLinkedList(LinkedList):

    def find_loop_start(self):
        # TODO: Implement me
        pass

# Unit Tests
class TestFindLoopStart(object):

    def test_find_loop_start(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: One element')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Two elements')
        linked_list.append(2)
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: Not a circular linked list: Three or more elements')
        linked_list.append(3)
        assert_equal(linked_list.find_loop_start(), None)

        print('Test: General case: Circular linked list')
        node10 = Node(10)
        node9 = Node(9, node10)
        node8 = Node(8, node9)
        node7 = Node(7, node8)
        node6 = Node(6, node7)
        node5 = Node(5, node6)
        node4 = Node(4, node5)
        node3 = Node(3, node4)
        node2 = Node(2, node3)
        node1 = Node(1, node2)
        node0 = Node(0, node1)
        node10.next = node3
        linked_list = MyLinkedList(node0)
        assert_equal(linked_list.find_loop_start(), node3)

        print('Success: test_find_loop_start')


def main():
    test = TestFindLoopStart()
    test.test_find_loop_start()


if __name__ == '__main__':
    main()

'''
Algorithm
    Use two references 'slow' and 'fast', initialized to the head
    Increment 'slow' and 'fast' until they meet
        'fast' is incremented twice as fast as 'slow'
            if 'fast'.next is None, we do not have a circular list
    When 'slow' and 'fast' meet, move 'slow' to the head
    Increment 'slow' and 'fast' one node at a time until they meet
    Where they meet is the start of the loop

    Complexity:
        Time: O(n)
        Space: O(1)
'''
# Solution
class MyLinkedListSolution(LinkedList):

    def find_loop_start(self):
        if self.head is None or self.head.next is None:
            return None

        slow = self.head
        fast = self.head
        while fast.next is not None:
            slow = slow.next
            fast = fast.next.next
            if fast is None:
                return None
            if slow == fast:
                break

        slow = self.head
        while slow != fast:
            slow = slow.next
            fast = fast.next
            if fast is None:
                return None
        return slow
