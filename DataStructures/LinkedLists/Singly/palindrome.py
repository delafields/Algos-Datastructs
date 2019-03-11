'''
Determine if a linked list is a palindrome

Constraints
    We can assume a non-circular singly linked list
    A single character is not a linked list
    We can assume we already have a linked list class
    We can use additional data structures
    We can assume this fits in memory

Test Cases
    Empty list -> False
    Single element list -> False
    Two or more element list, not a palindrome -> False
    General Case: Palindrome with even length -> True
    General Case: Palindrome with odd length -> True
'''
class MyLinkedList(LinkedList):

    def is_palindrome(self):
        # TODO: Implement Me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestPalindrome(object):

    def test_palindrome(self):
        print('Test: Empty list')
        linked_list = MyLinkedList()
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Single element list')
        head = Node(1)
        linked_list = MyLinkedList(head)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: Two element list, not a palindrome')
        linked_list.append(2)
        assert_equal(linked_list.is_palindrome(), False)

        print('Test: General case: Palindrome with even length')
        head = Node('a')
        linked_list = MyLinkedList(head)
        linked_list.append('b')
        linked_list.append('b')
        linked_list.append('a')
        assert_equal(linked_list.is_palindrome(), True)

        print('Test: General case: Palindrome with odd length')
        head = Node(1)
        linked_list = MyLinkedList(head)
        linked_list.append(2)
        linked_list.append(3)
        linked_list.append(2)
        linked_list.append(1)
        assert_equal(linked_list.is_palindrome(), True)

        print('Success: test_palindrome')


def main():
    test = TestPalindrome()
    test.test_palindrome()


if __name__ == '__main__':
    main()

'''
Algorithm
    Reverse the linked list
        Iterate through the current linked list
            Insert to front the current node into a new linked list
    Compare the reversed list with the original list
        Only need to compare the first half
        *Note - We could also do this iteratively,
                using a stack to effectively reverse the first half of the string

    Complexity:
        Time: O(n)
        Space: O(n)

'''
# Solution
class MyLinkedListSolution(LinkedList):

    def is_palindrome(self):
        if self.head is None or self.head.next is None:
            return False

        curr = self.head
        reversed_list = MyLinkedListSolution()
        length = 0

        # Reverse the linked list
        while curr is not None:
            reversed_list.insert_to_front(curr.data)
            length += 1
            curr = curr.next

        # Compare the reversed list with the original list
        # Only need to compare the first half
        iterations = length // 2
        curr = self.head
        curr_reversed = reversed_list.head
        for _ in range(iterations):
            if curr.data != curr_reversed.data:
                return False
            curr = curr.next
            curr_reversed = curr_reversed.next
        return True
