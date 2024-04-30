from vertex import Vertex


class Graph:
    # 图的抽象类
    def __init__(self):
        self.vertList = {}
        self.numVertices = 0

    def addVertex(self, key):
        pass

    def addEdge(self, f, t, cost=0):
        pass

    def getVertices(self):
        return self.vertList.keys()

    def __len__(self):
        return self.numVertices

    def __contains__(self, item):
        return item in self.vertList

    def __iter__(self):
        return iter(self.vertList.values())


class WeightDigraph(Graph):  # 带权有向图
    def addVertex(self, key):
        self.numVertices += 1
        newVertex = Vertex(key)
        self.vertList[key] = newVertex
        return newVertex

    def addEdge(self, f, t, cost=0):
        if f not in self.vertList:
            self.addVertex(f)
        if t not in self.vertList:
            self.addVertex(t)

        self.vertList[f].addNeighbor(self.vertList[t], cost)


if __name__ == '__main__':
    wg = WeightDigraph()

    for i in range(10):
        wg.addVertex(i)

    for i in range(9):
        wg.addEdge(i, i + 1)

    for v in wg:
        for w in v.getConnectTos():
            print(v.id, w.id, end='\t\n')
            print(v.getConnectTos()[w])
