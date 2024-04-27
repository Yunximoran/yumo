from functools import wraps


class Queue:
    def __init__(self):
        self.__vals = []
        self.__size = 0

    # 没有self不能调用self.__size
    # 有self会导致func传入异常
    @staticmethod
    def __addSize(func):
        @wraps(func)  # 导入functools中的wraps模块
        def wrapper(self, val):
            self.__size += 1
            func(self, val)

        return wrapper

    @staticmethod
    def __subSize(func):
        @wraps(func)
        def wrapper(self):
            self.__size -= 1
            return func(self)

        return wrapper

    @__addSize
    def addFront(self, val):
        self.__vals.append(val)

    @__addSize
    def addRear(self, val):
        self.__vals.insert(0, val)

    @__subSize
    def removeFront(self):
        return self.__vals.pop()

    @__subSize
    def removeRear(self):
        return self.__vals.pop(0)

    def isEmpty(self):
        return self.__vals == []

    def getVals(self):
        return self.__vals

    def Size(self):
        return self.__size


a = Queue()
print(a.Size())

a.addRear(1)
a.addRear(1)
a.addRear(1)
a.addRear(1)
print(a.Size())
a.removeRear()
a.removeRear()
a.removeRear()
print(a.Size())
