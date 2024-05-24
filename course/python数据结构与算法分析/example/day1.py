# sort

def bubbleSort(alist):
    pos = len(alist) - 1

    while pos > 0:
        for i in range(pos):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]

        pos -= 1


def shortBubbleSort(alist):
    pos = len(alist) - 1
    stop = False

    while pos > 0 and not stop:
        stop = True
        for i in range(pos):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
                stop = False


def selectSort(alist):
    # 每次循环在为排序的部分中选择最小值，进行插入
    for i in range(len(alist)):
        index = i
        for j in range(i, len(alist)):
            if alist[j] < alist[index]:
                alist[index] = alist[j]
                index = j

        alist[i], alist[index] = alist[index], alist[i]


def insertSort(alist):
    pos = len(alist)

    for i in range(1, len(alist)):
        current = alist[i]
        pos = i
        while pos > 0 and alist[pos - 1] > current:
            alist[pos] = alist[pos - 1]
            pos -= 1

        # alist[i], alist[pos] = alist[pos], alist[i]   不是交换，而是直接复制
        alist[pos] = current


def shellSort(alist):
    pass


def mergeSort(alist):
    if len(alist) > 1:
        midpoint = len(alist) // 2
        left = alist[:midpoint]
        right = alist[midpoint:]

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
            k += 1
            i += 1

        while j < len(right):
            alist[k] = right[j]
            k += 1
            j += 1


if __name__ == '__main__':
    data = [3, 2, 1, 5, 6, 4, 8, 7, 9]
    selectSort(data)
    print(data)
    print(data[: 3])
    print(data[3:])
