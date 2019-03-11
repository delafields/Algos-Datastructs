'''
Add two numbers whose digits are stored in a linked list in reverse order

Constraints
    We assume a non-circular singly linked list
    We expect the return to be in reverse order
    If one of the inputs is None, return None for invalid operation
    Numbers are not so large as to not fit in memory
    We assume we already have a linked list class
    We assume this fits in memory

Test Cases
    Empty list -> None
    Add values of different lengths
        Input 1: 6 -> 5 -> None
        Input 2: 9 -> 8 -> 7
        Input 3: 5 -> 4 -> 8
    Add values of same lengths
        Exercised from values of different lengths
        Done here for completeness
'''
# Implement
class MyLinkedList(LinkedList):

    def add_reverse(self, first_list, second_list):
        # TODO: Implement me
        pass

# Unit Tests
class TestAddReverse(object):

    def test_add_reverse(self):
        print('Test: Empty list(s)')
        assert_equal(MyLinkedList().add_reverse(None, None), None)
        assert_equal(MyLinkedList().add_reverse(Node(5), None), None)
        assert_equal(MyLinkedList().add_reverse(None, Node(10)), None)

        print('Test: Add values of different lengths')
        # Input 1: 6->5->None
        # Input 2: 9->8->7
        # Result: 5->4->8
        first_list = MyLinkedList(Node(6))
        first_list.append(5)
        second_list = MyLinkedList(Node(9))
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        assert_equal(result.get_all_data(), [5, 4, 8])

        print('Test: Add values of same lengths')
        # Input 1: 6->5->4
        # Input 2: 9->8->7
        # Result: 5->4->2->1
        first_head = Node(6)
        first_list = MyLinkedList(first_head)
        first_list.append(5)
        first_list.append(4)
        second_head = Node(9)
        second_list = MyLinkedList(second_head)
        second_list.append(8)
        second_list.append(7)
        result = MyLinkedList().add_reverse(first_list, second_list)
        assert_equal(result.get_all_data(), [5, 4, 2, 1])

        print('Success: test_add_reverse')


def main():
    test = TestAddReverse()
    test.test_add_reverse()


if __name__ == '__main__':
    main()

'''
Algorithm
    We could solve this iteratively or recursively.
    We'll use recursion
        This take extra space of O(m) of memory
        where m is recursion depth

    Base Case:
        If first and second lists are None and carry is zero
            Return None
    Recursive Case:
        Set value to carry
        Add both nodes' data to value
        Set the carry to 1 if value >= 10, else 0
        Set the remainder to value % 10
        Create a node with remainder
        Set node.next to a recursive call on the next nodes, passing in the carry
        Return node

    Complexity
        Time: O(n)
        Space: O(m), extra space for result and recursion depth

    Notes:
        Careful with adding if the lists differ
            Only add if a node is not None
            Alternatively, we could add trailing zeroes to the smaller list
'''
# Solution
class MyLinkedListSolution(LinkedList):

    def _add_reverse(self, first_node, second_node, carry):
        # Base Case
        if first_node is None and second_node is None and not carry:
            return None

        # Recursive Case
        value = carry
        value += first_node.data if first_node is not None else 0
        value += second_node.data if second_node is not None else 0
        carry = 1 if value >= 10 else 0
        value %= 10
        node = Node(value)
        node.next = self.add_reverse(
            first_node.next if first_node is not None else None,
            second_node.next if first_node is not None else None,
            carry
        )
        return node

        def add_reverse(self, first_list, second_list):
            # See constraints
            if first_list is None or second_list is None:
                return None
        head = self._add_reverse(first_list.head, second_list.head, 0)
        return MyLinked(head)
