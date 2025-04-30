class Node:
    def __init__(self, val):
        self.__val = val
        self.__next = None

    def __iter__(self):
        if self:
            if self.__next:
                for elem in self.__next:
                    yield elem
            yield self.__val

    def getVal(self):
        return self.__val

    def setVal(self, val):
        self.__val = val

    def getNext(self):
        return self.__next

    def setNext(self, Node):
        self.__next = Node


class Link:
    __head = None
    __size = 0

    @staticmethod
    def __addSize(func):
        def wrapper(self, val):
            func(self, val)
            self.__size += 1

        return wrapper

    @staticmethod
    def __subSize(func):
        def wrapper(self, val):
            res = func(self, val)
            print("res", res)
            if res:
                self.__size -= 1
            return res

        return wrapper

    def findNode(self, val):
        pass

    @__addSize
    def addNode(self, val):
        pass

    @__subSize
    def removeNode(self, val):
        current = self.__head
        previous = None

        found = False
        index = 0
        while current is not None and not found:
            if current.getVal() == val:
                found = True
            else:
                index += 1
                previous = current
                current = current.getNext()

        if found:  # 找到才会执行代码
            if previous:
                previous.setNext(current.getNext())
            else:
                self.__head = current.getNext()

            return current.getVal()

        return None

    def __iter__(self):
        return self.__head.__iter__()

    def __len__(self):
        return self.__size

    def __contains__(self, item):
        return self.findNode(item)

    @classmethod
    def __str__(cls):
        return cls.__name__
