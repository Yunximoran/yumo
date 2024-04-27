from .vertex import Vertex


class Graph:
    """
        抽象图

    @:param __vertList:
    @:param :
    """
    __vertList = {}
    __numVertices = 0

    def addVertex(self, key):
        """

        :param key:
        :return:
        """
        pass

    def addEdge(self, f, t, cost):
        pass

    def delVertex(self, key):
        pass

    def upVertex(self, OldKey, NewKey):
        pass

    def getVertices(self):
        return self.__vertList.keys()

    def __len__(self):
        return self.__numVertices

    def __iter__(self):
        return iter(self.__vertList.values())

    def __contains__(self, item):
        return item in self.__vertList


class WeightDigraph(Graph):
    """
        带权有向图
    """

    def addVertex(self, key):
        self._Graph__numVertices += 1
        newVertex = Vertex(key)
        self._Graph__vertList[key] = newVertex
        return newVertex

    def addEdge(self, f, t, cost=0):
        """
            创建连接
        :param f: 连接起点
        :param t: 连接终点
        :param cost: 权重
        :return: None
        """
        if f not in self._Graph__vertList:
            self.addVertex(f)
        if t not in self._Graph__vertList:
            self.addVertex(t)
        self._Graph__vertList[f].addNeighbor(self._Graph__vertList[t], cost)

    def delVertex(self, key):
        # 删除并取出对象
        delObj = self._Graph__vertList.pop(key)

        for vertex in self._Graph__vertList.values():  # 遍历图中其他对象
            if delObj in vertex.getConnectTos():  # 判断是否有关于当前对象的引用
                del vertex.getConnectTos()[delObj]  # 删除引用

        return delObj  # 返回当前对象

    def upVertex(self, OldKey, NewKey, cost=0):
        # 缺少对权重的更新


        OldVertex = self._Graph__vertList[OldKey]  # 去取当前顶点
        UpList = []
        for key in self._Graph__vertList:  # 获取其他顶点对当前顶点的引用
            if key == OldKey:
                continue
            if OldVertex in self._Graph__vertList[key].getConnectTos():
                UpList.append(key)  # 将引用信息加入UpList

        self.delVertex(OldKey)

        for CMSG in OldVertex.getConnectTos():
            if CMSG.id in self._Graph__vertList:
                self.addEdge(NewKey, CMSG.id, cost)

        for RMSG in UpList:
            self.addEdge(RMSG, NewKey, cost)
