# 冒泡排序
def bubbleSort(alist):
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[passnum]:
                alist[passnum], alist[i] = alist[i], alist[passnum]

    for i in range(len(alist)):
        for j in range(len(alist) - 1):
            pass


# 短冒泡排序
def shortBubbleSort(alist):
    pass


# 选择排序
def selectSort(alist):
    pass


# 插入排序
def insertSort(alist):
    pass


# 希尔排序
def shellSort(alist):
    pass


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
