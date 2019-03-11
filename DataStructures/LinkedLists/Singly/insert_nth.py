"""
 Insert Node at a specific position in a linked list
 head input could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.

Ex:
    Input
        None, data=3, position=0
        3 --> None, data=4, position=0
    Output
        3 --> None
        4 --> 3 --> None
"""
class Node(object):
    def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

# Implement
def insertNth(head, data, position):
    # TODO: Implement Me
    pass



# Solution
def insertNthSolution(head, data, position):

    if position ==0:
        return Node(data, head)

    curr = head
    while position > 1:
        curr = curr.next
        position -= 1
    curr.next = Node(data, head.next)

    return head
