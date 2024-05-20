

class Stack:
    def __init__(self):
        self.vals = []

    def push(self, val):
        self.vals.append(val)

    def peek(self):
        return self.vals[-1]

    def pop(self):
        return self.vals.pop()

    def isEmpty(self):
        return self.vals == []

    def size(self):
        return len(self.vals)
