from lib.datastructure.basic.queue import Queue


# 增删查改
class Vertex:
    distance = None
    pred = None
    color = None

    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectTo[nbr] = weight

    def getConnectTos(self):
        return self.connectTo

    def getId(self):
        return self.id

    def setDistance(self, distance):
        self.distance = distance

    def setPred(self, pred):
        self.pred = pred

    def setColor(self, color):
        self.color = color

    def getDistance(self):
        return self.distance

    def getPred(self):
        return self.pred

    def getColor(self):
        return self.color

    def __str__(self):
        return str(self.id) + '' + str([x.id for x in self.connectTo])

    # def __iter__(self):
    #     return iter(self.connectTo.values())


class Graph:
    def __init__(self):
        self.vertList = {}
        self.numVertex = 0

    def addVertex(self, key):
        self.numVertex += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def updateVertex(self, OldKey, NewKey):
        OldVertex = self.vertList[OldKey]  # 取出要更新的节点
        CacheTemp = []  # 存放其他节点对当前节点的引用
        for key in self.vertList:
            if OldVertex in self.vertList[key].getConnectTos():
                # 更新前遍历节点信息
                CacheTemp.append(key)

        self.removeVertex(OldKey)

        # 重建连接
        for x in OldVertex.getConnectTos():
            if x.id in self.vertList:
                self.addEdge(NewKey, x.id)
                # 其他节点指向更新节点的连接没有被记录， 更新没办法进行

        # 重建引用
        for edge in CacheTemp:
            self.addEdge(edge, NewKey)

    def removeVertex(self, key):

        reVertex = self.vertList.pop(key)  # 从图中删除并取出节点
        for vertex in self.vertList.values():
            # 遍历图中所有节点
            if reVertex in vertex.getConnectTos():
                # 移除其他节点中对删除节点的引用
                del vertex.getConnectTos()[reVertex]

        return reVertex

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)

    def getVertices(self):
        return self.vertList.keys()

    def __iter__(self):
        return iter(self.vertList.values())

    def __contains__(self, item):
        return item in self.vertList

    def __len__(self):
        return self.numVertex

    """
    Vertex类和Graph类都有一个字典类型容器存放节点对象，
    Graph的节点存放在value中
    Vertex的节点存放在key中
    """


def bfs(g, start):
    start.setDistance(0)
    start.setPred(None)
    vertQueue = Queue()
    vertQueue.enqueue(start)
    while len(vertQueue) > 0:
        currentVert = vertQueue.dequeue()
        for nbr in currentVert.getConnections():
            if nbr.getColor() == 'white':
                nbr.setColor('gray')
                nbr.setDistance(currentVert.getDistance() + 1)
                nbr.setPred(currentVert)
                vertQueue.enqueue(nbr)
        currentVert.setColor('black')


G = Graph()

G.addVertex("yumo1")
G.addVertex("yumo2")
G.addVertex("yumo3")

G.addEdge('yumo1', 'yumo2')
G.addEdge('yumo1', 'yumo3')
G.addEdge('yumo2', 'yumo3')
G.addEdge('yumo2', 'yumo1')
G.addEdge('yumo3', 'yumo1')

for i in G:
    print(id(i.getConnectTos()))
    # for j in i.connectTo:
    #     print("else:", j)

# print('\n update after')

# G.updateVertex('yumo1', 'yumo4')
# for i in G:
#     print(i)
# a = G.removeVertex('yumo1')
# print(a.id)
# [print(x.id) for x in a.connectTo]
#
# print('\n update after')
#
# G.updateVertex('yumo4', 'yumo5')
# for i in G:
#     print(i)
#
# print('\n update after')
#
# G.updateVertex('yumo5', 'yumo1')
# for i in G:
#     print(i)

# 更新后原来字典中默认的顺序会被改动
# 但应该问题不大，
