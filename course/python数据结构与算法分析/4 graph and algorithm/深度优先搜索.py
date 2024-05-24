# 骑士周游问题

from graph import WeightDigraph
from vertex import Vertex
from lib.datastructure.basic.stack import Stack

"""
knightGraph:
该函数将整个棋盘遍历了一遍？

当它访问棋盘的每一格时，都会调用辅助函数genLegalMoves来创建一个列表
用于记录从这一格开始的所有合理走法。
之后所有和合理走法都会被记录转换成图中的边。
另一个辅助函数posToNodeId将棋盘上的行列位置转换成图后，
"""


def knightGraph(bdSize):
    #
    ktGraph = WeightDigraph()

    for row in range(bdSize):
        for col in range(bdSize):
            # 这里获取到了两个位置 noteId， nid
            notdId = posToNodeId(row, col, bdSize)
            newPositions = genLegalMoves(row, col, bdSize)
            for e in newPositions:
                # e中只有两个元素
                # e中记录notdId的所有移动后的可能位置的坐标
                # 7
                nid = posToNodeId(e[0], e[1], bdSize)
                ktGraph.addEdge(notdId, nid)

    return ktGraph


def posToNodeId(row, col, bdSize):
    # 无实际意义， 只是为每个位置创建标签
    return (row * bdSize) + col


def genLegalMoves(x, y, bdSize):
    # genLegalMoves方法只记录棋子的可能走法，并不做棋子的移动操作
    newMoves = []
    # 对于任意位置的棋子，都有八条路线 [上， 下， 左， 右， 上左， 上右， 下左， 下右]
    moveOffsets = [(-1, -2), (-1, 2), (-2, -1), (-2, 1), (1, -2), (1, 2), (2, -1), (2, 1)]
    for i in moveOffsets:
        newX = x + i[0]
        newY = y + i[1]
        if legalCoord(newX, bdSize) and legalCoord(newY, bdSize):
            newMoves.append((newX, newY))

    return newMoves


def legalCoord(x, size):
    # 判断当前位置， 如果棋子行动后不在棋盘内则返回False
    return True if (0 <= x < size) else False


#
# kg = knightGraph(8)
# # 总共有64个顶点
# print(len(kg))  # kg中保存所有的位置信息
#
# # 怎么输出所有的边和连接个数
# count = 0
# for k in kg:
#     count += len(k.getConnectTos())
# # 连接是单向的，所以这里两个顶点间的连接是独立区分开的
# print(count)


def knightTour(n, path, u, limit):
    """

    :param n:
    :param path:
    :param u:
    :param limit:
    :return:
    """
    u.setColor('gray')

    path.append(u)
    if n < limit:
        # n 和 limit可比较
        # 当前深度和最大深度
        # u 应该是图中的某个节点
        # 获取当前顶点的所有连接
        nbrList = list(u.getConnectTos())
        i = 0
        done = False
        # 逐个访问这些顶点
        # 通过递归访问到最深处的顶点
        while i < len(nbrList) and not done:
            """
            循环递归执行knightTour
            if nbrList[i].getColor() == 'White' 不成立
            说明这是死路
            """
            if nbrList[i].getColor() == 'white':  # 第一次访问到最后一个节点是，还会执行该操作
                done = knightTour(n + 1, path, nbrList[i], limit)

            i += 1

        if not done:  # 准备回溯，回溯什么？？？
            # path是什么，列表？ 还是栈？
            path.pop()
            # path是什么？？？
            # 将u标记会白色
            u.setColor("white")
            # 将u标记会白色
            """
            DFS算法通过尽可能深地探索分支来构建搜索树
            
            两种实现：
            1、通过显式的禁止顶点被多次访问来直接解决骑士周游问题
            2、在构建搜索树时允许顶点被多次访问
            
            当DFS遇到思路时，退回到树中的倒2深的顶点，继续往其他方向移动
            """
    else:
        done = True
    return done

# start = Vertex()
# graph = WeightDigraph()
#
# knightTour(0, path, A, 6)
