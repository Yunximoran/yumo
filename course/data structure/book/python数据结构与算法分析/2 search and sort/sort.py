def bubbleSort(alist):  # 冒泡排序
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[passnum] > alist[i]:
                alist[passnum], alist[i] = alist[i], alist[passnum]


def shortBubbleSort(alist):  # 短冒泡排序
    exchanges = True

    passnum = len(alist) - 1

    while passnum > 0 and exchanges:
        exchanges = False  # 排序初始化为False
        # 如果本次循环没有进行交换，则说明排序已经完成，直接退出排序

        for i in range(passnum):
            if alist[i] > alist[passnum]:
                alist[passnum], alist[i] = alist[i], alist[passnum]
                exchanges = True


def selectSort(alist):  # 选择排序
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot - 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


def insertSort(alist):
    # 第一层循环从第二个元素开始遍历
    for index in range(1, len(alist)):
        currentvalue = alist[index]  # 获取当前值
        position = index  # 获取当前索引

        while position > 0 and alist[position - 1] > currentvalue:  # 如果alist[position] < currentvalue 说明需要交换
            alist[position] = alist[position - 1]   #
            position = position - 1

        alist[position] = currentvalue


def shellSort(alist):
    pass


def mergeSort(alist):
    pass
