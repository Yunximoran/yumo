

class Deque:
    def __init__(self):
        self.vals = []

    def addFront(self, val):
        self.vals.append(val)

    def addRear(self, val):
        self.vals.insert(0, val)

    def removeFront(self):
        return self.vals.pop()

    def remove(self):
        return self.vals.pop(0)

    def isEmpty(self):
        return self.vals == []

    def size(self):
        return len(self.vals)

