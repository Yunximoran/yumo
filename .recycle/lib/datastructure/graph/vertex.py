class Vertex:


    distance = None
    color = None
    pred = None

    def __init__(self, key):
        self.id = key
        self.__connectTo = {}

    def addNeighbor(self, nbr, weight=0):
        """
            创建连接，可以理解成链表或者数的next， 顶点可以有多个next
        :param nbr: 节点对象（Vertex）
        :param weight: 权重
        :return:
        """
        self.__connectTo[nbr] = weight

    def getId(self):
        return self.id

    def getConnectTos(self):
        return self.__connectTo

    def getWeight(self, nbr):
        return self.__connectTo[nbr]

    def getDistance(self):
        return self.distance

    def getColor(self):
        return self.color

    def getPred(self):
        return self.pred

    def setDistance(self, distance):
        self.distance = distance

    def setColor(self, color):
        self.color = color

    def setPred(self, pred):
        self.pred = pred

    def __str__(self):
        return str(self.id) + ' connectTo: ' \
            + str([x.id for x in self.__connectTo])
