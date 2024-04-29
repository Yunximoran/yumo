class Queue:
    def __init__(self):
        self.vals = []

    def enqueue(self, val):
        self.vals.append(val)

    def dequeue(self):
        return self.vals.pop(0)

    def isEmpty(self):
        return self.vals == []

    def size(self):
        return len(self.vals)
