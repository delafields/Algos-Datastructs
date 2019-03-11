"""
 Get Node data of the Nth Node from the end.
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the node data of the linked list in the below method.
"""
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Implement
def GetNode(head, position):
    pass

# Solution
def GetNodeSolution(head, position):
    if head is None:
        return None

    fast = head
    slow = head

    for _ in range(position):
        fast = fast.next
        if fast is None:
            return None

    while fast.next is not None:
        fast = fast.next
        slow = slow.next

    return slow.data
