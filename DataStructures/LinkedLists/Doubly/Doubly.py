class Node:

    def __init__(self, data, prev=None, next=None):
        self.data = data
        self.prev = prev
        self.next = next

    def __str__(self):
        return self.data

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        count = 0
        curr = self.head
        while curr is not None:
            count += 1
            curr = curr.next
        return count
