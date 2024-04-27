def binarySearch(alist, val):
    alist = sorted(alist)

    if len(alist) == 0:
        return False

    midpoint = len(alist) // 2
    if alist[midpoint] == val:
        return True
    else:
        if alist[midpoint] > val:
            return binarySearch(alist[:midpoint], val)
        if alist[midpoint] < val:
            return binarySearch(alist[midpoint + 1:], val)


def sequenceSearch(alist, val):
    found = False
    pos = 0
    while pos < len(alist) and not found:
        if alist[pos] == val:
            found = True
        else:
            pos += 1

    return found


class HashTable:

    def __init__(self):
        self.__size = 11
        self.__slots = [None] * self.__size
        self.__datas = [None] * self.__size

    def Init(self):
        self.__init__()

    def getSlots(self):
        return self.__slots

    def getDatas(self):
        return self.__datas

    def hashValue(self, key):
        return key % self.__size

    def show(self):
        print("Slots", self.__slots)
        print("Datas", self.__datas)

    def reHash(self, oldKey):
        return (oldKey + 1) % self.__size

    def __put(self, key, val):
        if None not in self.__slots:
            self.__size += 11
            self.__rebuild()
        hashValue = self.hashValue(key)
        if self.__slots[hashValue] == key:
            self.__datas[hashValue] = val

        if self.__slots[hashValue] is None:
            self.__slots[hashValue] = key
            self.__datas[hashValue] = val
        else:
            nextHash = self.reHash(hashValue)
            if self.__slots[nextHash] is not None and self.__slots[nextHash] != key:
                nextHash = self.reHash(nextHash)

            if self.__slots[nextHash] == key:
                self.__datas[nextHash] = val
            else:
                self.__slots[nextHash] = key
                self.__datas[nextHash] = val

    def __get(self, key):
        data = None

        startSlot = self.hashValue(key)
        pos = startSlot
        stop = False
        while not stop:
            if self.__slots[pos] == key:
                data = self.__datas[pos]
                break
            else:
                pos = self.reHash(pos)
                if pos == startSlot:
                    stop = True
        return data

    def __rebuild(self):
        slots = self.__slots
        datas = self.__datas

        self.__slots = [None] * self.__size
        self.__datas = [None] * self.__size

        for key, val in zip(slots, datas):
            self.__put(key, val)

    def __setitem__(self, key, value):
        self.__put(key, value)

    def __getitem__(self, item):
        return self.__get(item)

    def __len__(self):
        return len(self.__slots)

    def __contains__(self, item):
        return item in self.__slots
