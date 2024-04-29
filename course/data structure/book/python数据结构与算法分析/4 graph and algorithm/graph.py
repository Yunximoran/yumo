from vertex import Vertex


class Graph:
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
    pass
