class Queue:
    __vals = []
    __size = 0

    def enqueue(self, val):
        self.__size += 1
        self.__vals.append(val)

    def dequeue(self):
        self.__size -= 1
        return self.__vals.pop(0)

    def isEmpty(self):
        return self.__vals == []

    def getVals(self):
        return self.__vals

    def __len__(self):
        return self.__size

    def __iter__(self):
        return iter(self.__vals)

    def __contains__(self, item):
        return item in self.__vals
