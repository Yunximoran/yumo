class Node:
    def __init__(self, val):
        self.__val = val
        self.__next = None

    def __iter__(self):
        return self

    def getVal(self):
        return self.__val

    def getNext(self):
        return self.__next

    def setVal(self, val):
        self.__val = val

    def setNext(self, node):
        self.__next = node


class UnorderedList:
    __head = None
    __size = 0

    def __init__(self):
        pass

    def __len__(self):
        return self.__size

    def __contains__(self, item):
        return self.selectNode(item)

    def __iter__(self):
        current = self.__head
        while current is not None:
            yield current.getVal()
            current = current.getNext()

    def insertNode(self, val):
        temp = Node(val)
        temp.setNext(self.__head)
        self.__head = temp

    def removeNode(self, val):
        current = self.__head
        previous = None
        found = False
        while current is not None and not found:
            if current.getVal() == val:
                found = False

            else:
                previous = current
                current = current.getNext()

        if previous:
            previous.setNext(current.getNext())
        else:
            self.__head = current.getNext()

        return current.getVal()

    def selectNode(self, val):
        current = self.__head
        found = False
        while current is not None and not found:
            if current.getVal() == val:
                found = True
            else:
                current = current.getNext()
        return found

    def updateNode(self, oldVal, newVal):
        current = self.__head
        found = False
        while current is not None and not found:
            if current.getVal() == oldVal:
                found = True
            else:
                current = current.getNext()

        if found:
            current.setVal(newVal)
        else:
            self.insertNode(newVal)


if __name__ == '__main__':
    ol = UnorderedList()
    ol.insertNode(1)
    ol.insertNode(2)
    print(1 in ol)  # out:True
    ol.updateNode(1, 3)
    print(ol.selectNode(3))  # out: True
    print(ol.selectNode(2))  # out: True

    print(1 in ol)  # out: False
    print(2 in ol)  # out: True

    for i in ol:
        print(i)
