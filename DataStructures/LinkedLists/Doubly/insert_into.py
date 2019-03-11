"""
Insert a node into a sorted doubly linked list
head could be None as well for empty list
return the head node of the updated list

Ex
    Input
        2
        5
        4
    Output
        2 -> 4 -> 5

"""
class Node:
    def __init__(self, data=None, next_node=None, prev_node = None):
    self.data = data
    self.next = next_node
    self.prev = prev_node

# Implement

def SortedInsert(head, data):
    pass


# Solution
def SortedInsertSolution(head, data):
    node = Node(data)
    if head is None:
        return node

    current = head

    while current.next is not None:
        if node.data >= current.data and node.data <= current.next.data:
            current.next.prev = node
            node.next = current.next
            current.next = node
            return head
        current = current.next

    node.prev = current
    current.next = node
    return head
