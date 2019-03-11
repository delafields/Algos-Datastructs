class Queue:
    #init
    #isEmpty
    #size
    #enqueue
    #dequeue

    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)

    def enqueue(self, item):
        return self.items.insert(0, item)

    def dequeue(self):
        return self.items.pop()
