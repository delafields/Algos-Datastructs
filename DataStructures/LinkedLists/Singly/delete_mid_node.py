'''
Delete a node in the middle, given only access to that node

Constraints
    We can assume a non-circular singly linked list
    If the node being deleted is the final node,
        we make it a dummy with value None
    We assume we already have a linked list class

Test Cases
    Delete on empty list -> None
    Delete None -> None
    Delete on one node -> [None]
    Delete on multiple nodes
'''
# Implement
class MyLinkedList(LinkedList):

    def delete_node(self, node):
        # TODO: Implement me
        pass

# Unit Tests
from nose.tools import assert_equal


class TestDeleteNode(object):

    def test_delete_node(self):
        print('Test: Empty list, null node to delete')
        linked_list = MyLinkedList(None)
        linked_list.delete_node(None)
        assert_equal(linked_list.get_all_data(), [])

        print('Test: One node')
        head = Node(2)
        linked_list = MyLinkedList(head)
        linked_list.delete_node(head)
        assert_equal(linked_list.get_all_data(), [None])

        print('Test: Multiple nodes')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node1)
        assert_equal(linked_list.get_all_data(), [1, 4, 2])

        print('Test: Multiple nodes, delete last element')
        linked_list = MyLinkedList(None)
        node0 = linked_list.insert_to_front(2)
        node1 = linked_list.insert_to_front(3)
        node2 = linked_list.insert_to_front(4)
        node3 = linked_list.insert_to_front(1)
        linked_list.delete_node(node0)
        assert_equal(linked_list.get_all_data(), [1, 4, 3, None])

        print('Success: test_delete_node')


def main():
    test = TestDeleteNode()
    test.test_delete_node()


if __name__ == '__main__':
    main()

'''
Algorithm
    We need two pointers: one to the current node, one to the next node
    We copy the next node's data to the current node's data (effectively deleting the current node).
    Then update the current node's next pointer

    set curr.data = next.data
    set curr.next to next.next

    Complexity:
        Time: O(1)
        Space: O(1)
'''
# Solution
class MyLinkedListSolution(LinkedList):

    def delete_node(self, node):
        if node is None:
            return
        if node.next is None:
            node.data = None
        else:
            node.data = node.next.data
            node.next = node.next.next
