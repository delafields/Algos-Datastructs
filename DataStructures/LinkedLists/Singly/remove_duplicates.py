'''
Remove Duplicates from a linked list

Constraints
    Assume it is a non-circular, singly linked list
    You cannot insert None values
    Assume we already have a linked list class
    Can use additional data structures (implement both)
    Can assume it fits in memory

Test Cases
    Empty linked list -> []
    One element linked list -> [element]
    General case with no duplicates
    General case with duplicates
'''
# Implement
class MyLinkedList(LinkedList):

    def remove_dupes(self):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestRemoveDupes(object):

    def test_remove_dupes(self, linked_list):
        print('Test: Empty list')
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One element list')
        linked_list.insert_to_front(2)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [2])

        print('Test: General case, duplicates')
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(2)
        linked_list.insert_to_front(3)
        linked_list.insert_to_front(1)
        linked_list.insert_to_front(1)
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

        print('Test: General case, no duplicates')
        linked_list.remove_dupes()
        assert_equal(linked_list.get_all_data(), [1, 3, 2])

        print('Success: test_remove_dupes\n')


def main():
    test = TestRemoveDupes()
    linked_list = MyLinkedList(None)
    test.test_remove_dupes(linked_list)


if __name__ == '__main__':
    main()

'''
Algorithm: Hash Map Lookup

    Loop through each node
    For each nodde
        If the node's value is in the hash map
        Delete the node
    Else
        Add the node's value to the hash map

    Complexity:
        Time: O(n)
        Space: O(n)

Algorithm: In-Place

    For each node
        Compare node with every other node
            Delete nodes that match current node
    *Note - We'll need to use a 'runner' to check every other node and compare it to the current node

    Complexity:
        Time: O(n^2)
        Space: O(1)
'''

class MyLinkedListSolution(LinkedList):

    def remove_dupes(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set()
        while node is not None:
            if node.data not in seen_data:
                seen_data.add(node.data)
                prev = node
                node = node.next
            else:
                prev.next = node.next
                node = node.next

    def remove_dupes_single_pointer(self):
        if self.head is None:
            return
        node = self.head
        seen_data = set({node.data})
        while node.next is not None:
            if node.next.data in seen_data:
                node.next = node.next.next
            else:
                seen_data.add(node.next.data)
                node = node.next

    def remove_dupes_in_place(self):
        curr_node = self.head
        while curr_node is not None:
            runner = curr_node
            while runner.next is not None:
                if runner.next.data == curr_node.data:
                    runner.next = runner.next.next
                else:
                    runner = runner.next
            curr_node = curr_node.next
