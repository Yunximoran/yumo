class Vertex:
    def __init__(self, key):
        self.id = key
        self.connectTo = {}

    def addNeighbor(self, nbr, weight=0):
        self.connectTo[nbr] = weight

    def __str__(self):
        return str(self.id) + ' connectTos: ' + str([x.id for x in self.connectTo])

    def getConnectTos(self):
        return self.connectTo

    def getDistance(self):
        return

    def getPred(self):
        return

    def getColor(self):
        return

    def setDistance(self, distance):
        pass

    def setPred(self, pred):
        pass

    def setColor(self, color):
        pass
