from graph import WeightDigraph
from vertex import Vertex
from lib.datastructure.basic.queue import Queue


def buildGraph(worFile):
    """
        词梯问题构建单词关系图

    :param worFile:
    :return:
    """
    d = {}
    g = WeightDigraph()

    wfile = open("", 'r')
    for line in wfile:
        word = line[:-1]
        # 创建词桶
        for i in range(len(word)):
            bucket = word[:i] + '_' + word[i + 1:]
            if bucket in d:
                d[bucket].append(word)
            else:
                d[bucket] = [word]
    # 为桶一个桶中的单词添加顶点和边
    for bucket in d.keys():
        for word1 in d[bucket]:
            for word2 in d[bucket]:
                if word1 != word2:
                    # addEdge方法自带创建顶点， 建立连接
                    g.addEdge(word1, word2)

    return g


# 广度优先搜索
def bfs(g, start):
    """
        广度优先搜索
    :param g: Graph
    :param start: Vertex
    :return:
    """
    start.setDistance(0)
    start.setPred(None)

    verQueue = Queue()
    # 将起始节点加入队列
    verQueue.enqueue(start)

    while len(verQueue) > 0:  # 所以这里用while
        # 利用队列实现递归
        # 取出起始节点
        currentVert = verQueue.dequeue()
        # 遍历所有与当前节点相连接的其他顶点
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')  # 访问中标记为黑色
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                verQueue.enqueue(nbr)
                """
                队列能保证所有顶点的层级都是连续的
                [0, 1, 1, 1, 1, 2, 2, 2, 2, 2, 2, 2, 2, 3, 3,...., 3]
                
                栈不行？栈应该是什么效果？？？ 先进后出
                使用栈的话应该就是递归
                
                # 终归不是递归
                    该循环会将所有白色节点加入队列， 并标记成灰色节点
                    进入下次循环后，  
                    栈也可以？？？
                    # 栈不行，队列可以保证每次循环都是同一层的顶点
                    如果是栈的话，就变成深度了
                    # 所以也不是递归
                    # 递归会深入到
                """
                # 只有白色节点会被加入队列
                # 这里用栈是不是也可以？？？

        currentVert.setColor("black")

    """
        给定图G和起点， 通过访问G中与s之间存在路径的顶点。
    
    BFS特性：
        在访问完所有与s相距为k的顶点之后再去访问与s相距k+1的顶点。
    
    BFS以每次生成一层的方式构建一棵树。他会在访问任意一个孙节点之前将起点的所有子节点添加进来
    
    执行过程：
    
    1、BFS会将顶点标记为白色、灰色或黑色
    2、初始化所有顶尖为白色
    3、当节点第一次被访问时，标记为灰色
    4、当BFS完成对该顶点的访问时，标记为黑色
    
    * 当顶点标记为黑色时，意味着没有白色顶点与之相连。
    
    有点类似递归，逐个访问顶点中，当顶点被标记为黑色后，回到上一个顶点，访问其他白色顶点，知道所有白色顶点标记为黑色
    在回退到上一个节点
    """
