class Deque:
    def __init__(self):
        self.__vals = []
        self.__size = 0

    @staticmethod
    def __addSize(func):
        def wrapper(*args, **kwargs):
            func(*args, **kwargs)
            args[0].__size += 1

        return wrapper

    @staticmethod
    def __subSize(func):
        def wrapper(*args, **kwargs):
            args[0].__size -= 1
            return func(*args, **kwargs)

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

    def __len__(self):
        return self.__size

    def __iter__(self):
        # 使类可迭代
        return iter(self.__vals)

    def __contains__(self, item):
        """
            python中的魔术方法，用于实现一个容器类型的对象的成员检查操作

            当使用in关键字检查一个元素是否存在于一个容器中时，python会自
            动调用这个方法
        :param item:
        :return:
        """
        return item in self.__vals
