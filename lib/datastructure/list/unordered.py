from .abstract.link import Link, Node


class UnorderedList(Link):

    def findNode(self, val):
        current = self._Link__head
        found = False
        while current is not None and not found:
            if current.getVal() == val:
                found = True
            else:
                current = current.getNext()

        return found

    def addNode(self, val):
        super().addNode(val)

        temp = Node(val)
        temp.setNext(self._Link__head)
        self._Link__head = temp
