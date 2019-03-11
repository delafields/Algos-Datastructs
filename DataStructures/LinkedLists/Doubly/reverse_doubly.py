"""
Reverse a doubly linked list
head could be None as well for empty list
return the head node of the updated list

Ex:
    Input
        None
        None <-- 2 <--> 4 <--> 6 --> None
    Output
        None
        None <-- 6 <--> 4 <--> 6 --> None
"""

class Node:
    def __init__(self, data=None, next_node=None, prev_node = None):
    self.data = data
    self.next = next_node
    self.prev = prev_node

def Reverse(head):
    pass



# Solution
def ReverseSolution(head):
    if head is None:
        return None

    current = head
    prev = None

    while current is not None:
        temp = current.next
        current.prev = temp
        current.next = prev
        prev = current
        current = temp

    return prev
