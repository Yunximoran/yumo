import copy


class HashTable:
    __size = 11

    def __init__(self):
        self.slots = [None] * self.__size
        self.datas = [None] * self.__size

    def __len__(self):
        count = 0
        for slot in self.slots:
            if slot is not None:
                count += 1
        return count

    def __contains__(self, item):
        hashVal = self.getHashVal(item)
        return True if self.slots[hashVal] is not None and self.slots[hashVal] == item else False

    def getHashVal(self, key):
        return key % self.__size

    def reHashVal(self, oldVal):
        return (oldVal + 1) % self.__size

    def put(self, key, val):
        hashVal = self.getHashVal(key)
        if self.slots[hashVal] is None:
            self.slots[hashVal] = key
            self.datas[hashVal] = val
        else:
            if self.slots[hashVal] == key:
                self.datas[hashVal] = val
            else:
                nextVal = self.reHashVal(hashVal)
                while self.slots[nextVal] is not None and self.slots[nextVal] != key:
                    nextVal = self.reHashVal(nextVal)
                    if hashVal == nextVal:
                        self.__rebuild()

                if self.slots[nextVal] is None:
                    self.slots[nextVal] = key
                    self.datas[nextVal] = val
                else:
                    self.datas[nextVal] = val

    def __rebuild(self):
        slots = copy.deepcopy(self.slots)
        datas = copy.deepcopy(self.datas)
        self.__size += 11
        self.__init__()
        for slot, data in zip(slots, datas):
            # print(slot, data)
            self.put(slot, data)

    def get(self, key):
        data = None
        startSlots = self.getHashVal(key)
        stop = False
        found = False
        position = startSlots
        while self.slots[position] is not None and not stop and not found:
            if self.slots[position] == key:
                data = self.datas[position]
                found = True
            else:
                position = self.reHashVal(position)
                if position == startSlots:
                    stop = True

        return data

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)

