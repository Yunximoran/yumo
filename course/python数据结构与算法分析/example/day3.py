import random


class MyHash:
    size = 11

    def __init__(self):
        self.slots = [None] * self.size
        self.datas = [None] * self.size

    def put(self, key, val):

        if None not in self.slots:
            self.size += 11
            self.__reBuildHash()

        hashValue = self.__getHash(key)
        nextValue = None
        if self.slots[hashValue] == key:
            self.datas[hashValue] = val
        elif self.slots[hashValue] is None:
            self.slots[hashValue] = key
            self.datas[hashValue] = val
        else:
            nextValue = self.__reHash(hashValue)
            while self.slots[nextValue] is not None and self.slots[nextValue] != key:
                nextValue = self.__reHash(nextValue)

            if self.slots[nextValue] == key:
                self.datas[nextValue] = val
            else:
                self.slots[nextValue] = key
                self.datas[nextValue] = val

    def __reBuildHash(self):
        slots = self.slots
        datas = self.datas

        while slots is not []:
            key = slots.pop()
            val = datas.pop()
            self.put(key, val)

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getHash(self, Key):
        return Key % self.size

    def __reHash(self, oldKey):
        return (oldKey + 1) % self.size

    def __len__(self):
        count = 0
        for i in self.slots:
            if i is not None:
                count += 1

        return count


class TreeNode:
    def __init__(self, key, val, parent=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

    def isRoot(self):
        return True if self.parent is None else False

    def isLeaf(self):
        return True if self.left is None and self.right is None else False

    def isLeft(self):
        return True if self.parent and self.parent.left == self else False

    def isRight(self):
        return True if self.parent and self.parent.right == self else False

    def hasLeft(self):
        return True if self.left else False

    def hasRight(self):
        return True if self.right else False

    def hasAnyChild(self):
        return True if not (self.left or self.right) else False

    def hasBothChild(self):
        return True if self.left and self.right else False

    def replaceNodeData(self, k, v, lc, rc):
        self.key = k
        self.val = v
        self.left = lc
        self.right = rc
        if self.hasLeft():
            self.left.parent = self

        if self.hasRight():
            self.right.parent = self

    def findSuccessor(self):
        succ = None
        if self.hasRight():
            succ = self.findMin()
        else:
            if self.parent:
                if self.isLeft():
                    succ = self.parent
                else:
                    self.parent.right = None
                    self.parent.findSuccessor()
                    self.parent.right = self

    def findMin(self):
        current = self
        while current.hasLeft():
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.left = None
            else:
                self.parent.right = None
        else:
            if self.hasLeft():
                if self.isLeft():
                    self.left.parent = self.parent
                    self.parent.left = self.left
                else:
                    self.left.parent = self.parent
                    self.parent.right = self.left
            else:
                if self.isLeft():
                    self.right.parent = self.parent
                    self.parent.left = self.right

                else:
                    self.right.parent = self.parent
                    self.parent.right = self.right

    def __iter__(self):
        if self:
            if self.hasLeft():
                for elem in self.left:
                    yield elem

            yield self

            if self.hasRight():
                for elem in self.right:
                    yield elem

    def __str__(self):
        return f"value:{self.val}"


class Vertex:
    def __init__(self, key):
        self.key = key
        self.connects = {}

    def buildConnect(self, vertex, weight):
        self.connects[vertex] = weight

    def getConnects(self):
        return self.connects

    def __str__(self):
        return f"key{self.key}"


class Graph:
    def __init__(self):
        self.vertList = {}
        self.size = 0

    def addVertex(self, key):
        vertex = Vertex(key)
        self.vertList[key] = vertex
        self.size += 1
        return vertex

    def addEdge(self, start, end, weight=0):
        if start not in self.vertList:
            self.addVertex(start)
        if end not in self.vertList:
            self.addVertex(end)

        self.vertList[start].buildConnect(self.vertList[end], weight)


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def __len__(self):
        return self.size

    def length(self):
        return self.size

    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size += 1

    def __put(self, key, val, current):
        if current.key > key:
            if current.hasLeft():
                self.__put(key, val, current.left)
            else:
                current.left = TreeNode(key, val, current)
        else:
            if current.hasRight():
                self.__put(key, val, current.right)
            else:
                current.right = TreeNode(key, val, current)

    def get(self, key):
        res = None
        if self.root:
            res = self.__get(key, self.root)
        return res

    def __get(self, key, current):
        if current is None:
            return None

        elif current.key == key:
            return current
        elif current.key > key:
            return self.__get(key, current.left)
        else:
            return self.__get(key, current.right)

    def delete(self, key):
        if self.size > 1:
            position = self.__get(key, self.root)
            if position:
                self.remove(position)
                self.size -= 1
            else:
                pass
        elif self.size == 1 and self.root == key:
            self.root = None
        else:
            pass

    def remove(self, current):
        if current.isLeaf():
            if current.isLeft():
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.hasAnyChild():
            if current.hasLeft():
                if current.isLeft():
                    current.left.parent = current.parent
                    current.parent.left = current.left
                elif current.isRihgt():
                    current.left.parent = current.parent
                    current.parent.right = current.left

                else:
                    current.replaceNodeData(
                        current.left.key,
                        current.left.val,
                        current.left.left,
                        current.left.right
                    )
            else:
                if current.isLeft():
                    current.right.parent = current.parent
                    current.parent.left = current.right

                elif current.isRight():
                    current.right.parent = current.parent
                    current.parent.right = current.right
                else:
                    current.replaceNodeData(
                        current.right.key,
                        current.right.val,
                        current.right.left,
                        current.right.right
                    )
        else:
            succ = current.findSuccessor()
            succ.spliceOut()
            current.key = succ.key
            current.val = succ.val

    def __contains__(self, item):
        return True if self.get(item) else False

    def __iter__(self):
        return self.root.__iter__()


if __name__ == '__main__':
    H = MyHash()
    count = set()
    for i in range(100):
        index = random.randint(0, 99)
        H[index] = 1
        count.add(index)

    print(len(H))
    print(len(count))
