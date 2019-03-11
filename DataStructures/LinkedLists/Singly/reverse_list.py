# Linked List Reversal

# Problem

# Write a function to reverse a Linked List in place.
# The function will take in the head of the list as input and
# return the new head of the list.


# You are given the Node class
class Node:
    def __init__(self, initdata):
        self.data = initdata
        self.nextnode = None


# And a short list of Nodes
a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d


# Solution
def reverse(head):
    current = head
    previous = None
    nextnode = None

    while current:
        nextnode = current.nextnode  # copy before overwritting

        current.nextnode = previous

        previous = current
        current = nextnode

    return previous


print(d.nextnode.data)
print(c.nextnode.data)
print(b.nextnode.data)
