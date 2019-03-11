'''
Find the kth to last element of a linked list

Constraints
    We can assume a non-circular singly linked list
    We can assume k is a valid integer
    If k = 0, return the last element
    If k is >= len(linked list) return None
    Cannot use additional data structures
    We can assume we already have a linked list class

Test Cases
    Empty List -> None
    k is >= length linked list -> None
    One element, k = 0 -> element
    General case with many elements, k < length of linked list
'''
# Implement
class MyLinkedList(LinkedList):

    def kth_to_last_elem(self, k):
        # TODO: Implement Me
        pass

# Unit Tests
from nose.tools import assert_equal


class Test(object):

    def test_kth_to_last_elem(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        assert_equal(linked_list.kth_to_last_elem(0), None)

        print('Test: k >= len(list)')
        assert_equal(linked_list.kth_to_last_elem(100), None)

        print('Test: One element, k = 0')
        head = Node(2)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.kth_to_last_elem(0), 2)

        print('Test: General case')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(5)
        linked_list.insert_to_front(7)
        assert_equal(linked_list.kth_to_last_elem(2), 3)

        print('Success: test_kth_to_last_elem')


def main():
    test = Test()
    test.test_kth_to_last_elem()


if __name__ == '__main__':
    main()

'''
Algorithm
    Setup two pointers, fast and slow
    Give fast a headstart, incrementing it once if k = 1, twice if k = 2...
    Increment both pointers until fast reaches the end
    Return the value of slow

    Complexity:
        Time: O(n)
        Space: O(1)
'''
# Solution
class MyLinkedListSolution(LinkedList):

    def kth_to_last_elem(self, k):
        if self.head is None:
            return None

        fast = self.head
        slow = self.head

        # Give fast a headstart, incrementing it
        # once for k=1, twice for k=2, etc..
        for _ in range(k):
            fast = fast.next
            # If k >= num elements, return None
            if fast is None:
                return None

        # Increment both pointers until fast reaches the end
        while fast.next is not None:
            fast = fast.next
            slow = slow.next
        return slow.data
