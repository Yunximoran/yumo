class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

    def getVal(self):
        return self.val

    def getNext(self):
        return self.next

    def setVal(self, val):
        self.val = val

    def setNext(self, next):
        self.next = next

    def __iter__(self):
        if self:
            if self.next:
                for elem in self.next:
                    yield elem
            yield self.val


class Link:
    def __init__(self):
        self.head = None

    def search(self, item):
        current = self.head

        found = False
        while current is not None and not found:
            if current.getVal() == item:
                found = True
            else:
                current = current.getNext()

        return found

    def addNode(self, val):
        pass

    def remove(self, val):
        pass

    def __len__(self):
        count = 0
        for _ in self.head:
            count += 1
        return count

    def __contains__(self, item):
        return self.search(item)

    def __iter__(self):
        return self.head.__iter__()

class UnorderedList(Link):
    def addNode(self, val):
        temp = Node(val)
        temp.setNext(self.head)
        self.head = temp

    def remove(self, val):
        current = self.head
        previous = None
        found = False

        while not found:
            if current.getVal() == val:
                found = True
            else:
                previous = current
                current = current.getNext()
        if found:
            if previous:
                previous.setNext(current.getNext())
            else:
                self.head = current.getNext()
        else:
            print('no found')


class OrderList(Link):
    def addNode(self, val):
        current = self.head
        previous = None

        stop = False
        while current is not None and not stop:
            if current.getVal() < val:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(val)

        if previous:
            temp.setNext(current)
            previous.setNext(temp)
        else:
            temp.setNext(self.head)
            self.head = temp

    def remove(self, val):
        current = self.head
        previous = None

        found = False
        stop = False

        while not found and not stop:
            if current.getVal() == val:
                found = True
            else:
                if current.getVal() < val:
                    stop = True
                else:
                    previous = current
                    current = current.getNext()

        if found:
            if previous:
                previous.setNext(current.getNext())
            else:
                self.head = current.getNext()
        else:
            print('not found')


if __name__ == '__main__':

    ul = UnorderedList()

    ul.addNode(1)
    ul.addNode(2)
    ul.addNode(3)
    ul.addNode(4)
    ul.addNode(8)

    for val in ul:
        print(val)

    print(len(ul))

    print('\n')

    ol = OrderList()

    ol.addNode(3)
    ol.addNode(2)
    ol.addNode(7)
    ol.addNode(4)
    ol.addNode(1)

    for val in ol:
        print(val)

    print(len(ol))


    print()
    ol.remove(8)
    for val in ol:
        print(val)

    print(5 in ol)
    print(4 in ol)

    print(1 in ul)
    print(9 in ul)

    print(ol)
