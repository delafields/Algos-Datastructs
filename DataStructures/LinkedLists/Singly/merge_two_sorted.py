"""
 Merge two linked lists
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.

Ex
    Inputs
        1 -> 3 -> 5 -> 6 -> None
        2 -> 4 -> 7 -> None

        15 -> None
        12 -> None

        None
        1 -> 2 -> None

    Output
        1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> None
        12 -> 15 -> None
        1 -> 2 -> None
"""
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Implement
def MergeLists(headA, headB):
    # TODO: Implement me
    pass


# Solution
def MergeListsSolution(headA, headB):
    if not headA:
        return headB
    if not headB:
        return headA

    # Create a first node
    head = result = Node()

    # Merge elements into a new list
    while headA or headB:
        if headA and (not headB or headA.data <= headB.data):
            result.next = Node(headA.data)
            headA = headA.next
        else:
            result.next = Node(headB.data)
            headB = headB.next

        result = result.next

    return head.next
