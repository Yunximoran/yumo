def sequenceSearch(alist, item):
    found = False
    pos = 0
    while pos <= len(alist) and not found:
        if alist[pos] == item:
            found = True
        else:
            pos += 1
    return found


def binarySearch(alist, item):
    midpoint = len(alist) // 2

    if midpoint > 1:
        if alist[midpoint] == item:
            return True
        else:
            if alist[midpoint] > item:
                return binarySearch(alist[:midpoint], item)
            else:
                return binarySearch(alist[midpoint + 1:], item)
    return False


class HashTable:
    size = 11

    def __init__(self):
        self.slots = [None] * self.size
        self.datas = [None] * self.size

    def hashvalue(self, key):
        return key % self.size

    def rehash(self, oldKey):
        return (oldKey + 1) % self.size

    def put(self, key, val):
        hashval = self.hashvalue(key)

        if self.slots[hashval] is None:
            self.slots[hashval] = key
            self.datas[hashval] = val
        else:
            if self.slots[hashval] == key:
                self.data[hashval] = val

            else:
                nextval = self.rehash(hashval)
                while self.slots[nextval] is not None and self.slots[nextval] != key:
                    nextval = self.rehash(nextval)

                if self.slots[nextval] is None:
                    self.slots[nextval] = key
                    self.datas[nextval] = val
                else:
                    self.datas[nextval] = val

    def get(self, key):
        startslot = self.hashvalue(key)
        data = None

        pos = startslot

        while self.slots[pos] is not None:
            #
            if self.slots[pos] == key:
                data = self.datas[pos]
            else:
                pos = self.rehash(pos)
                if pos == startslot:
                    break

        return data

    def __setitem__(self, key, value):
        self.put(key, value)

    def __getitem__(self, item):
        return self.get(item)
