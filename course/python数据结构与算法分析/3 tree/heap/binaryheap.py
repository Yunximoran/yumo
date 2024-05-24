# 二叉堆
"""
堆 特殊的二叉树

他的每个节点的值都 大于[小于] 等于 其子节点的值。
                 |   |
               大根[小根] 堆

堆通常用于实现排序和优先队列
"""

class BinaryHeap:
    def __init__(self):
        self.heapList = []
        self.currentSize = 0

    def insert(self, k):
        """
        将元素加入列表最简单的办法就是append
        优点： 保证完全树的性质
        缺点： 破坏堆的数据结构
        解决办法：
            1、通过比较新元素与其父元素来重新获得堆的结构性质。
                如果新元素小于父元素，就将二者交换
        :return:
        """
        self.heapList.append(k)
        self.currentSize += 1
        self.percUp(self.currentSize)

    def percUp(self, i):
        # 二叉结构中，任意节点 的 父元素 是 当前节点 整除 2
        # i // 2
        while i // 2 > 0:
            if self.heapList[i] < self.heapList[i // 2]:
                temp = self.heapList[i // 2]
                self.heapList[i // 2] = self.heapList[i]
                self.heapList[i] = temp
            i // 2

    """
    移除最小元素
    只需要移除根节点与他最小子节点即可
    重复节点与其子节点的交换过程，
    直到节点比其他两个子节点都小
    """

    def percDown(self, i):
        mc = self.minChild(i)   # 获取当前节点最小子节点索引

        # 堆的结构性质， 左节点 小于 右节点 ？？？ 不一定 ！
        while i * 2 < self.currentSize:
            if self.heapList[i] > self.heapList[mc]:
                temp = self.heapList[i]
                self.heapList[i] = self.heapList[mc]
                self.heapList[mc] = temp
            # 为什么要将i赋值给mc
            i = mc

    def minChild(self, i):
        if 2 * i + 1 > self.currentSize:
            return i * 2
        else:
            if self.heapList[i * 2] < self.heapList[i * 2 + 1]:
                return i * 2
            else:
                return i * 2 + 1

    def delMin(self):
        reVal = self.heapList[1]
        # 用最后一个元素将第一个元素覆盖
        self.heapList[1] = self.heapList[self.currentSize]
        self.currentSize -= 1  # 堆长度 - 1
        self.heapList.pop()  # 删除最后一个元素
        self.percDown(1)
        return reVal
