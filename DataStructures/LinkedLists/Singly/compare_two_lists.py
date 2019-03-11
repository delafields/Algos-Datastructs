"""
Compare two linked lists for equality
 head could be None as well for empty list
 Return 0 if not equal, 1 if equal
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.

Ex:
    Inputs
        None, 1 -> None
        1 -> 2 -> None, 1 -> 2 -> None
    Output
        0
        1
"""
class Node:
    def __init__(self, data=None, next_node=None):
        self.data = data
        self.next = next_node

# Implement
def CompareLists(headA, headB):
    # TODO: Implement Me
    pass


# Solution
def CompareListsSolution(headA, headB):

    while headA and headB:
        if headA.data != headB.data:
            return 0
        headA, headB = headA.next, headB.next

    if headA is None and HeadB is None:
        return 1
    else:
        return 0
