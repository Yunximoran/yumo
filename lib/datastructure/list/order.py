from .abstract.link import Link, Node


class OrderList(Link):

    def findNode(self, val):
        current = self._Link__head

        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.getVal() == val:
                found = True
            else:
                if current.getVal() < val:
                    stop = True
                else:
                    current = current.getNext()

        return found

    def addNode(self, val):
        super().addNode(val)
        current = self._Link__head
        previous = None

        stop = False
        while current is not None and not stop:
            if current.getVal() <= val:
                stop = True
            else:
                previous = current
                current = current.getNext()

        temp = Node(val)
        if previous:
            previous.setNext(temp)
            temp.setNext(current)
        else:
            temp.setNext(self._Link__head)
            self._Link__head = temp
