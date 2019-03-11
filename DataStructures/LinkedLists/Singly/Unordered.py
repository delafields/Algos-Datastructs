'''
Implement a linked-list with insert/append/find/delete/length/print methods

Constraints:
    Assume it is non-circular, signly linked
    Keep track of just the head
    Cannot insert None Values

Tests:
    Insert None to Front
    Insert to front of an empty list
    Insert to front to a list with >= 1 element
    Find a None
    Find in an empty list
    Find in a list with >= 1 matching elements
    Find in a list with no matches
    Delete a None
    Delete in an empty List
    Delete in a list with >= 1 matching elements
    Delete in a list with no matches
    Length of zero or more elements
    Print an empty List
    Print a list w/ >= 1 elements
'''
# Implement
class Node:

    def __init__(self, data, next_node=None):
        pass
        # TODO: Implement me

    def __str__(self):
        pass
        # TODO: Implement me


class LinkedList:

    def __init__(self, head=None):
        pass
        # TODO: Implement me

    def __len__(self):
        pass
        # TODO: Implement me

    def insert_to_front(self, data):
        pass
        # TODO: Implement me

    def append(self, data):
        pass
        # TODO: Implement me

    def find(self, data):
        pass
        # TODO: Implement me

    def delete(self, data):
        pass
        # TODO: Implement me

    def print_list(self):
        pass
        # TODO: Implement me

    def get_all_data(self):
        pass
        # TODO: Implement me

# Unit Tests
from nose.tools import assert_equal


class TestLinkedList(object):

    def test_insert_to_front(self):
        print('Test: insert_to_front on an empty list')
        linked_list = LinkedList(None)
        linked_list.insert_to_front(10)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: insert_to_front on a None')
        linked_list.insert_to_front(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: insert_to_front general case')
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        assert_equal(linked_list.get_all_data(), ['bc', 'a', 10])

        print('Success: test_insert_to_front\n')

    def test_append(self):
        print('Test: append on an empty list')
        linked_list = LinkedList(None)
        linked_list.append(10)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: append a None')
        linked_list.append(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: append general case')
        linked_list.append('a')
        linked_list.append('bc')
        assert_equal(linked_list.get_all_data(), [10, 'a', 'bc'])

        print('Success: test_append\n')

    def test_find(self):
        print('Test: find on an empty list')
        linked_list = LinkedList(None)
        node = linked_list.find('a')
        assert_equal(node, None)

        print('Test: find a None')
        head = Node(10)
        linked_list = LinkedList(head)
        node = linked_list.find(None)
        assert_equal(node, None)

        print('Test: find general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        node = linked_list.find('a')
        assert_equal(str(node), 'a')

        print('Test: find general case with no matches')
        node = linked_list.find('aaa')
        assert_equal(node, None)

        print('Success: test_find\n')

    def test_delete(self):
        print('Test: delete on an empty list')
        linked_list = LinkedList(None)
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), [])

        print('Test: delete a None')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.delete(None)
        assert_equal(linked_list.get_all_data(), [10])

        print('Test: delete general case with matches')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        linked_list.delete('a')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print('Test: delete general case with no matches')
        linked_list.delete('aa')
        assert_equal(linked_list.get_all_data(), ['bc', 10])

        print('Success: test_delete\n')

    def test_len(self):
        print('Test: len on an empty list')
        linked_list = LinkedList(None)
        assert_equal(len(linked_list), 0)

        print('Test: len general case')
        head = Node(10)
        linked_list = LinkedList(head)
        linked_list.insert_to_front('a')
        linked_list.insert_to_front('bc')
        assert_equal(len(linked_list), 3)

        print('Success: test_len\n')


def main():
    test = TestLinkedList()
    test.test_insert_to_front()
    test.test_append()
    test.test_find()
    test.test_delete()
    test.test_len()


if __name__ == '__main__':
    main()

'''
Algorithm
    Insert To Front
        If the data we are inserting is None, return
        Create a node with the input data, set node.next to head
        Assign the head to the node

        Complexity:
            Time: O(1)
            Space: O(1)

    Append
        If the data we are inserting is None, return
        Create a node with the input data
        If list is empty
            Assign the head to the node
        Else
            Iterate to the end of the list
            Set the final node's next to the new node

        Complexity:
            Time: O(n)
            Space: O(1)

    Find
        If the data we are finding is None, return
        If the list is empty, return
        For each node
            If the value is a match, return it
            Else, move to the next node

        Complexity:
            Time: O(n)
            Space: O(1)

    Delete
        If the data we are deleting is None, return
        If the list is empty, return
        For each node, keep track of previous and current node
            If the value we are deleting is a match in the current node
                Update the previous node's next pointer to the current node's next pointer
                We don't need to explicitly delete in Python
            Else, move on to the next node
        *Alternative: we could avoid the use of two pointers by evaluating the current node's next value
            If the next value is a match, set the current node's next to next.next
            Special care needs to be taken to delete the next node

        Complexity:
            Time: O(n)
            Space: O(1)

    Length
        For each node increase the length counter

        Complexity:
            Time: O(n)
            Space: O(1)

    Print
        For each node print the node's value

        Complexity:
            Time: O(n)
            Space: O(1)
'''
# Solution
class NodeSolution:

    def __init__(self, data, next=None):
        self.next = next
        self.data = data

    def __str__(self):
        return self.data

class LinkedListSolution:

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        curr = self.head
        counter = 0
        while curr is not None:
            counter += 1
            curr = curr.next
        return counter

    def insert_to_front(self, data):
        if data is None:
            return None
        node = NodeSolution(data, self.head)
        self.head = node
        return node

    def append(self, data):
        if data is None:
            return None
        node = NodeSolution(data)
        if self.head is None:
            self.head = node
            return node
        curr_node = self.head
        while curr_node.next is not None:
            curr_node = curr_node.next
        curr_node.next = node
        return node

    def find(self, data):
        if data is None:
            return None
        curr_node = self.head
        while curr_node is not None:
            if curr_node.data == data:
                return curr_node
            curr_node = curr_node.next
        return None

    def delete(self, data):
        if data is None:
            return
        if self.head is None:
            return
        if self.head.data == data:
            self.head = self.head.next
            return
        prev_node = self.head
        curr_node = self.head.next
        while curr_node is not None:
            if curr_node.data == data:
                prev_node.next = curr_node.next
                return
            prev_node = curr_node
            curr_node = curr_node.next

    def delete_alt(self, data):
        if data is None:
            return
        if self.head is None:
            return
        curr_node = self.head
        if curr_node.data == data:
            curr_node = curr_node.next
            return
        while curr_node.next is not None:
            if curr_node.next.data == data:
                curr_node.next = curr_node.next.next
                return
            curr_node = curr_node.next

    def print_list(self):
        curr_node = self.head
        while curr_node is not None:
            print(curr_node.data)
            curr_node = curr_node.next

    def get_all_data(self):
        curr_node = self.head
        data = []
        while curr_node is not None:
            data.append(curr_node.data)
            curr_node = curr_node.next
        return data
