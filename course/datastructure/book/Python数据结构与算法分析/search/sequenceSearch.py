def sequenceSearch(alist, item):
    pos = 0
    while pos <= len(alist):
        if alist[pos] == item:
            return True
    return False


