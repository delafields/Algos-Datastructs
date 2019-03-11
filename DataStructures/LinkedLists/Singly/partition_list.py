'''
Partition a linked list around a value x,
such that all nodes < x come before all nodes >= x

Constraints
    We can assume this is a non-circular singly linked list
    We expect the funtion to return a new list
    We assume the input x is valid
    We assume we already have a linked list class
    We can create additional data structures
    We assume this fits in memory

Test Cases
    Empty List -> []
    One element list -> [element]
    Left linked list is empty
    Right linked list is empty
    General Case
        Partition = 10
        Input: 4, 3, 7, 8, 10, 1, 10, 12
        Output: 4, 3, 7, 8, 1, 10, 10, 12
'''
# Implement
class MyLinkedList(LinkedList):

    def partition(self, data):
        # TODO: Implement Me
        pass

# Unit Tests
class TestPartition(object):

    def test_partition(self):
        print('Test: Empty list')
        linked_list = MyLinkedList(None)
        linked_list.partition(10)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One element list, left list empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(0)
        assert_equal(linked_list.get_all_data(), [5])

        print('Test: Right list is empty')
        linked_list = MyLinkedList(Node(5))
        linked_list.partition(10)
        assert_equal(linked_list.get_all_data(), [5])

        print('Test: General case')
        # Partition = 10
        # Input: 4, 3, 13, 8, 10, 1, 14, 10, 12
        # Output: 4, 3, 8, 1, 10, 10, 13, 14, 12
        linked_list = MyLinkedList(Node(12))
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(14)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(10)
        linked_list.insert_to_front(8)
        linked_list.insert_to_front(13)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(4)
        partitioned_list = linked_list.partition(10)
        assert_equal(partitioned_list.get_all_data(),
                     [4, 3, 8, 1, 10, 10, 13, 14, 12])

        print('Success: test_partition')


def main():
    test = TestPartition()
    test.test_partition()


if __name__ == '__main__':
    main()

'''
Algorithm
    Create left and right linked lists
    For each element in the list
        If elem < x, append to the left list
        Else, append to the right list
    Merge left and right list

    Complexity:
        Time: O(n)
        Space: O(n)
'''
# Solution
class MyLinkedListSolution(LinkedList):

    def partition(self, data):
        if self.head is None:
            return

        left = MyLinkedListSolution(None)
        right = MyLinkedListSolution(None)
        curr_node = self.head

        # Build the left and right lists
        while curr_node is not None:
            if curr_node.data < data:
                left.append(curr_node.data)
            elif curr_node.data == data:
                right.insert_to_front(curr_node.data)
            else:
                right.append(curr_node.data)
            curr_node = curr_node.next

        curr_left = left.head
        if curr_left is None:
            return right
        else:
            # Merge the two lists
            while curr_left.next is not None:
                curr_left = curr_left.next
            curr_left.next = right.head
            return left
