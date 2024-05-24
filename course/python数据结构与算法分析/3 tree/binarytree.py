class Node:
    def __init__(self, key, val, parent=None):
        self.key = key
        self.val = val
        self.parent = parent
        self.left = None
        self.right = None

    def __iter__(self):
        if self:
            if self.left:
                for elem in self.left:
                    yield elem
            if self.right:
                for elem in self.right:
                    yield elem
            yield self

    def replaceNodeData(self, key, val, lc, rc):
        # 替换节点数据
        self.key = key
        self.val = val
        self.setLeftChild(lc)
        self.setRightChild(rc)

        # 这里应该有用到逻辑上的知识点，为什么要替换，原来的子节点绑定的父节点不还是当前节点？？？
        # 变量的作用域
        if self.hasLeftChild():
            # 如果左子节点存在， 将左子节点的父节点进行更新
            self.left.parent = self

        if self.hasRightChild():
            # 如果右子节点存在， 将右子节点的父节点进行更新
            self.right.parent = self
        """
        替换方法的作用是更新当前节点的数据
        
        由于数据变动，子节点的连接可能出现问题
        所以需要将当前节点与子节点的连接进行更新
        """

    def getLeftChild(self):
        return self.left

    def getRightChild(self):
        return self.right

    def setLeftChild(self, leftChild):
        self.left = leftChild

    def setRightChild(self, rightChild):
        self.right = rightChild

    def isRoot(self):
        return True if self.parent is None else False

    def isLeaf(self):
        return True if self.left is None and self.right is None else False

    def isLeftChild(self):
        return True if self.parent is not None and self.parent.left == self else False

    def isRightChild(self):
        return True if self.parent is not None and self.parent.right == self else False

    def hasLeftChild(self):
        return True if self.left is not None else False

    def hasRightChild(self):
        return True if self.right is not None else False

    def hasAnyChild(self):
        return True if not (self.right or self.left) else False

    def hasBothChild(self):
        return True if self.right and self.left else False

    def findSuccessor(self):
        succ = None
        if self.hasRightChild():
            # 如果删除节点右子节点存在， 则替换节点是右子树中的最小节点
            # 如果没有右节点且当前节点是父节点的左子节点，则替换节点是当前节点的父节点
            #
            succ = self.right.findMin()

            """
            left < root < right
            # 右子树的最小节点不会比左子树的最大节点小
            # 删除某个节点后要保证规则
            """
        else:  # 没有右节点
            # 否则判断父节点是否存在
            if self.parent:
                if self.isLeftChild():
                    # 父节点存在，且当前节点是左节点
                    # 则succ是当前节点
                    succ = self.parent
                else:
                    # 当前节点是右节点
                    # 将当前节点与父节点的连接暂时取消
                    # 递归执行findSuccessor()方法，在父节点中找到
                    # 替换节点就是要在树中找到 介于左右节点之间的的节点
                    # 调用父节点的findSuccessor()
                    # 将父节点的右节点连接断开
                    # 避免递归进入父节点的右子中
                    # 一直向上遍历父节点，直到节点是左子节点，返回该节点的父节点作为替换节点
                    self.parent.right = None
                    succ = self.parent.findSuccessor()
                    # 找到节点后，递归开始回溯， 执行一下代码重新建立与各自右节点的连接
                    self.parent.right = self
        return succ

    def findMin(self):
        current = self
        while current.hasLeftChild():
            current = current.left
        return current

    def spliceOut(self):
        if self.isLeaf():
            if self.isLeftChild():
                self.parent.left = None
            else:
                self.parent.right = None

        else:
            if self.hasLeftChild():
                if self.isLeftChild():
                    self.left.parent = self.parent
                    self.parent.left = self.left
                elif self.isRightChild():
                    self.left.parent = self.parent
                    self.parent.right = self.left
                else:
                    self.replaceNodeData(
                        self.left.key,
                        self.left.val,
                        self.left.left,
                        self.left.right
                    )
            else:
                if self.isLeftChild():
                    self.left.parent = self.parent
                    self.parent.right = self.left
                elif self.isRightChild():
                    self.right.parent = self.parent
                    self.parent.right = self.right
                else:
                    self.replaceNodeData(
                        self.right.key,
                        self.right.val,
                        self.right.left,
                        self.right.right
                    )

    def __str__(self):
        return f"{self.key}, {self.val}"


class BinaryTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def __iter__(self):
        return self.root.__iter__()

    def put(self, key, val):
        if self.root:
            self.__put(key, val, self.root)
        else:
            self.root = Node(key, val)

        self.size += 1

    def __put(self, key, val, currentNode):
        if key < currentNode.key:
            # 如果key 小于 当前节点 的key，添加左节点
            if currentNode.hasLeftChild():  # 左节点存在
                self.__put(key, val, currentNode.getLeftChild())
            else:
                # 创建一个新的节点，连接到当前节点的左节点中
                currentNode.left = Node(key, val, parent=currentNode)
        elif key > currentNode.key:
            if currentNode.hasRightChild():
                self.__put(key, val, currentNode.getRightChild())
            else:
                currentNode.right = Node(key, val, parent=currentNode)

    def get(self, key):
        if self.root:
            res = self.__get(key, self.root)
            if res:
                return res
            else:
                return None
        else:
            return None

    def __get(self, key, currentNode):
        if currentNode is None:
            return None
        elif currentNode.key == key:
            return currentNode
        else:
            if currentNode.key > key:
                return self.__get(key, currentNode.left)
            elif currentNode.key < key:
                return self.__get(key, currentNode.right)

    """
    待解决：
        添加重复键时，更新数据
    """

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

    def __contains__(self, item):
        return True if self.__get(item, self.root) else False

    def delete(self, key):
        if self.size > 1:
            nodeToRemove = self.get(key)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size -= 1
            else:
                raise KeyError("Error key not in tree")
        elif self.size == 1 and self.root.key == key:
            self.root = None
            self.size = 0
        else:
            raise KeyError("Error key not in tree")

    @staticmethod
    def remove(Node):
        if Node.isLeaf():
            # 没有子节点
            # 判断当前节点是上一个节点的左节点，还是右节点
            # 取消当前节点与父节点的连接
            if Node.isLeftChild():
                Node.parent.left = None
            else:
                Node.parent.right = None

        elif Node.hasAnyChild():
            # 当前节点只有一个子节点
            if Node.hasLeftChild():  # 当前节点只有左子节点
                if Node.isLeftChild():
                    # 如果当前节点是父节点的左子节点
                    # 删除父节点与当前节点的连接
                    # 将当前节点的子节点的父节点设置为当前节点的父节点
                    # 当前节点的父节点的左子节点设置为当前节点的子节点
                    Node.left.parent = Node.parent
                    Node.parent.left = Node.left
                elif Node.isRightChild():
                    Node.left.parent = Node.parent
                    Node.parent.right = Node.left

                else:  # 不是左子节点 也不是 右子节点 ？？？ 根节点
                    # 将子节点的数据替换到根节点中
                    Node.replaceNodeData(
                        Node.left.key,
                        Node.left.val,
                        Node.left.left,
                        Node.left.right
                    )
            else:  # 只有有右子节点
                if Node.isLeftChild():
                    Node.right.parent = Node.parent
                    Node.parent.left = Node.right
                elif Node.isRightChild():
                    Node.right.parent = Node.parent
                    Node.parent.right = Node.right
                else:
                    Node.replaceNode(
                        Node.right.key,
                        Node.right.val,
                        Node.right.left,
                        Node.right.right
                    )

        else:  # 删除节点中有两个子节点是最复杂的情况
            # 这意味这删除节点后需要找到合适的替换节点
            succ = Node.findSuccessor()
            succ.spliceOut()
            Node.key = succ.key
            Node.val = succ.val

    def __delitem__(self, key):
        self.delete(key)

