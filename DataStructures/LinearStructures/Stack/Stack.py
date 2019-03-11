class Stack:
    #init
    #pop
    #push
    #peek
    #isempty
    def __init__(self):
        self.items = []

    def pop(self):
        return self.items.pop()

    def push(self, item):
        return self.items.append(item)

    def peek(self):
        return self.items[-1]

    def isEmpty(self):
        return self.items == []

    def size(self):
        return len(self.items)
