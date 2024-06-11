class TreeNode:
    def __init__(self, key, val, parent=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

    def setLeft(self, nlc):
        self.left = nlc

    def setRight(self, nrc):
        self.right = nrc

    def setParent(self, np):
        self.parent = np

    def setKey(self, nk):
        self.key = nk

    def setVal(self, nv):
        self.val = nv

    def getLeft(self):
        return self.left

    def getRight(self):
        return self.right

    def getParent(self):
        return self.parent

    def getKey(self):
        return self.key

    def getVal(self):
        return self.val

    def isRoot(self):
        return True if self.parent is None else False

    def isLeaf(self):
        # 左右子节点同时为空
        return True if self.left is None and self.right is None else False

    def isLeft(self):
        # 父节点存在 且 父节点 的 左子节点 指向 当前节点
        return True if self.parent is not None and self.parent.left == self else False

    def isRight(self):
        return True if self.parent is not None and self.parent.right == self else False

    def hasParent(self):
        return True if self.parent is not None else False

    def hasLeft(self):
        return True if self.left is not None else False

    def hasRight(self):
        return True if self.right is not None else False

    def hasAnyChild(self):
        return True if not (self.left or self.right) else False

    def hasBothChild(self):
        return True if self.left and self.right else False

    def findSuccessor(self):
        succ = None
        if self.hasRight():
            succ = self.findMin()
        else:
            if self.parent:
                if self.isLeft():
                    succ = self.parent
                else:
                    self.parent.setRight(None)
                    self.parent.findSuccessor()
                    self.parent.setRight(self)
        return succ

    def findMin(self):
        current = self
        while current.hasLeft():
            current = current.getLeft()

        return current

    def SpliceOut(self):
        if self.isLeaf():
            if self.isLeft():
                self.parent.setLeft(None)
            else:
                self.parent.setRight(None)
        elif self.hasAnyChild():
            if self.hasLeft():
                if self.isLeft():
                    self.parent.setLeft(self.getLeft())
                else:
                    self.parent.setRight(self.getLeft())
                self.left.setParent(self.getParent())
            else:
                if self.isLeft():
                    self.parent.setLeft(self.getRight())
                else:
                    self.parent.setRight(self.getRight())
                self.right.setParent(self.getParent())

    def replaceNodeData(self, key, val, lc, rc):
        self.setKey(key)
        self.setVal(val)
        self.setLeft(lc)
        self.setRight(rc)

        if self.hasLeft():
            self.left.setParent(self)

        if self.hasRight():
            self.right.setParent(self)

    def __str__(self):
        return f"{self.key}"  # , val: {self.val}"

    def __iter__(self):
        if self:
            # 中序遍历返回的一定是顺序表？
            if self.hasLeft():
                for elem in self.getLeft():
                    yield elem
            yield self
            if self.hasRight():
                for elem in self.getRight():
                    yield elem


class Tree:
    __SIZE = 0

    def __init__(self):
        self.root = None

    def Set(self, key, value):
        if self.root is not None:
            self.__Set(key, value, self.root)
        else:
            self.root = TreeNode(key, value)

        self.__SIZE += 1

    def __Set(self, key, val, current):
        if current.key > key:
            if current.hasLeft():
                self.__Set(key, val, current.getLeft())
            else:
                current.setLeft(TreeNode(key, val, parent=current))
        else:
            if current.hasRight():
                self.__Set(key, val, current.getRight())
            else:
                current.setRight(TreeNode(key, val, parent=current))

    def Get(self, key):
        res = None
        if self.root:
            res = self.__Get(key, self.root)

        return res

    def __Get(self, key, current):
        if current is None:
            return None
        ckey = current.key
        if ckey == key:
            return current
        else:
            if ckey > key:
                return self.__Get(key, current.getLeft())
            else:
                return self.__Get(key, current.getRight())

    def Del(self, key):
        if self.__SIZE > 0:
            delNode = self.__Get(key, self.root)
            if delNode is not None:
                self.__Del(delNode)
                self.__SIZE -= 1
            else:
                raise KeyError("Error, key not in tree")
        elif self.__SIZE == 1 and self.root.key == key:
            self.root = None
            self.__SIZE -= 1
        else:
            raise KeyError("Error, key not in tree")

    @staticmethod
    def __Del(current):
        if current.isLeaf():
            if current.isLeft():
                current.parent.setLeft(None)
            else:
                current.parent.setRight(None)

        elif current.hasAnyChild():
            if current.hasLeft():
                if current.isLeft():
                    current.left.setParent(current.getParent())
                    current.parent.setLeft(current.getLeft())
                elif current.isRight():
                    current.left.setParent(current.getParent())
                    current.parent.setRight(current.getLeft())
                else:
                    current.replaceDataNode(
                        current.left.key,
                        current.left.val,
                        current.left.left,
                        current.left.right
                    )
            else:
                if current.isLeft():
                    current.right.setParent(current.getParent())
                    current.parent.setLeft(current.getRight())
                elif current.isRight():
                    current.right.setParent(current.getParent())
                    current.parent.setRight(current.getRight())
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

    def __setitem__(self, key, value):
        self.Set(key, value)

    def __getitem__(self, key):
        return self.Get(key)

    def __delitem__(self, key):
        self.Del(key)

    def __len__(self):
        return self.__SIZE

    def __contains__(self, item):
        return self.Get(item)

    def __iter__(self):
        return self.root.__iter__()
