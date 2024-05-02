# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]


# 短冒泡排序
def shortBubbleSort(alist):
    stop = False

    pos = len(alist) - 1
    while pos > 0 and not stop:
        stop = True
        for i in range(pos):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                stop = False


# 选择排序
def selectSort(alist):
    for i in range(len(alist)):
        positionMin = i
        for j in range(i, len(alist)):
            if alist[j] < alist[positionMin]:
                positionMin = j

        alist[i], alist[positionMin] = alist[positionMin], alist[i]


# 插入排序
def insertSort(alist):
    for i in range(1, len(alist)):
        current = alist[i]
        index = i
        while index > 0 and alist[index - 1] > current:
            alist[index] = alist[index - 1]
            index -= 1

        alist[index] = current


# 希尔排序
def shellSort(alist):
    sub = len(alist) // 2
    while sub > 0:
        sub //= 2


# 归并排序
def mergeSort(alist):
    if len(alist) > 1:
        mid = len(alist) // 2
        left = alist[:mid]
        right = alist[mid:]

        mergeSort(left)
        mergeSort(right)

        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                alist[k] = left[i]
                i += 1
            else:
                alist[k] = right[j]
                j += 1

            k += 1

        while i < len(left):
            alist[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            alist[k] = right[j]
            j += 1
            k += 1

# 快速排序
