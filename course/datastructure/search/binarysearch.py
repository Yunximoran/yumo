def binarySearch(alist, item):
    midpoint = len(alist) // 2
    if alist[midpoint] == item:
        return True
    else:
        if item < alist[midpoint]:
            return binarySearch(alist[:midpoint], item)
        else:
            return binarySearch(alist[midpoint + 1:], item)


