class Node:

    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        return self.data

class LinkedList:

    def __init__(self, head=None):
        self.head = head

    def __len__(self):
        counter = 0
        curr_node = self.head
        while curr_node is not None:
            counter += 1
            curr_node = curr_node.next
        return counter

    def find(self, item):
        curr_node = self.head
        found = False
        stop = False
        while curr_node is not None and not found and not stop:
            if curr_node.data == item:
                found = True
            else:
                if curr_node.data > item:
                    stop = True
                else:
                    curr_node = curr_node.next
        return found

    def add(self, item):
        curr_node = self.head
        prev_node = None
        stop = False
        while curr_node is not None and not stop:
            if curr_node.data > item:
                stop = True
            else:
                prev_node = curr_node
                curr_node = curr_node.next

        temp = Node(item)
        if prev_node == None:
            temp.next = self.head
            self.head = temp
        else:
            temp.next = curr_node
            prev_node.next = temp
