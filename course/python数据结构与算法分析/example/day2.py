class Stack:
    def __init__(self):
        self.vals = []

    def push(self, val):
        self.vals.append(val)

    def peek(self):
        return self.vals[-1]

    def pop(self):
        return self.vals.pop()

    def size(self):
        return len(self.vals)

    def isEmpty(self):
        return self.vals == []


class Queue:
    def __init__(self):
        self.vals = []

    def enqueue(self, val):
        self.vals.insert(0, val)

    def dequeue(self):
        return self.vals.pop()

    def size(self):
        return len(self.vals)

    def isEmpty(self):
        return self.vals == []


class Deque:
    def __init__(self):
        self.vals = []

    def addFront(self, val):
        self.vals.append(val)

    def addRear(self, val):
        self.vals.insert(0, val)

    def removeFrond(self):
        return self.vals.pop()

    def removeRear(self):
        return self.vals.pop(0)

    def size(self):
        return len(self.vals)

    def isEmpty(self):
        return self.vals == []


class MyHash:
    size = 11

    def __init__(self):
        self.slots = [None] * self.size
        self.datas = [None] * self.size

    def put(self, key, val):
        hashvalue = self.hashfunc(key)
        if self.slots[hashvalue] is None:
            self.slots[hashvalue] = key
            self.datas[hashvalue] = val

        else:
            if self.slots[hashvalue] == key:
                self.datas[hashvalue] = val
            else:
                nexthash = self.rehash(hashvalue)
                while self.slots[nexthash] is not None and self.slots[nexthash] != key:
                    nexthash = self.rehash(nexthash)

                if self.slots[nexthash] is None:
                    self.slots[nexthash] = key
                    self.datas[nexthash] = val
                else:
                    self.datas[nexthash] = val

    def rehash(self, oldKey):
        return (oldKey + 1) % self.size

    def hashfunc(self, key):
        return key % self.size


class Node:
    def __init__(self, val):
        self.val = val
        self.next = None


class List:
    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, val):
        temp = Node(val)
        temp.nextNode = self.head
        self.head = temp
        self.size += 1

    def get(self, val):
        current = self.head
        while current is not None:
            if current.val == val:
                return current.val
            else:
                current = current.next

    def remove(self, val):
        current = self.head
        previous = None
        while current.val != val and current is not None:
            previous = current
            current = current.next

        if previous:
            previous.next = current.next
        else:
            self.head = current.next


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

    def findSuccessor(self):
        succ = None
        if self.hasRight():
            succ = self.findMind()
        else:
            if self.parent:
                if self.isLeft():
                    succ = self.parent
                else:
                    succ.parent.right = None
                    succ.parent.findSuccessor()
                    succ.parent.right = self
        return succ

    def findMind(self):
        current = self
        while current.hasLeft():
            current = current.left
        return current

    def SpliceOut(self):
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

    def replaceDataNode(self, key, val, lc, rc):
        self.key = key
        self.val = val
        self.left = lc
        self.right = rc
        if self.hasLeft():
            self.left.parent = self

        if self.hasRight():
            self.right.parent = self

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
        return f"key: {self.key}, val: {self.val}"


class Tree:
    def __init__(self):
        self.root = None
        self.size = 0

    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = TreeNode(key, val)

        self.size += 1

    def __put(self, key, val, current):
        if current.key == key:
            current.key = key
            current.val = val
        else:
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
        if self.root:
            res = self.__get(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def __get(self, key, current):
        if current is None:
            return None
        else:
            if current.key == key:
                return current
            elif current.key > key:
                return self.__get(key, current.left)
            else:
                return self.__get(key, current.right)

    def delete(self, key):
        if self.size > 1:
            item = self.__get(key, self.root)
            if item:
                self.remove(item)
                self.size -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size -= 1
        else:
            raise KeyError("Error, key not in tree")

    @staticmethod
    def remove(current):
        if current.isLeaf():
            if current.isLeft():
                # 根节点？？？没有父节点？？？
                current.parent.left = None
            else:
                current.parent.right = None
        elif current.hasAnyChild():
            if current.hasLeft():
                if current.isLeft():
                    current.left.parent = current.parent
                    current.parent.left = current.left
                elif current.isRight():
                    current.left.parent = current.parent
                    current.parent.right = current.left
                else:
                    current.repalceDataNode(
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
                    current.replaceDataNode(
                        current.right.key,
                        current.right.val,
                        current.right.left,
                        current.right.right
                    )
        else:
            succ = current.findSuccessor()
            succ.SpliceOut()
            current.key = succ.key
            current.val = succ.val

    def __iter__(self):
        return self.root.__iter__()

    def __contains__(self, item):
        return self.get(item)
        # res = self.get(item)
        # if res:
        #     res.key = item
        #     return True
        # else:
        #     return False

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __delitem__(self, key):
        self.delete(key)

    def __len__(self):
        return self.size


if __name__ == '__main__':
    tree = Tree()

    tree[1] = 3
    tree[3] = 9
    tree[2] = 4
    tree[5] = 25
    tree[8] = 64
    for i in tree:
        print(i)

    print(4 in tree)
    print(99 in tree)
    print(1 in tree)
