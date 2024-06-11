def bubbleSort(alist):
    for i in range(1, len(alist)):
        for j in range(i):
            if alist[j] < alist[j - 1]:
                alist[j], alist[j - 1] = alist[j - 1], alist[j]


def shortBubbleSort(alist):
    pos = len(alist)
    stop = False
    while pos > 0 and not stop:
        stop = True
        for i in range(pos):
            if alist[pos] < alist[pos + 1]:
                alist[pos + 1], alist[pos] = alist[pos], alist[pos + 1]
                stop = False


def selectSort(alist):
    for i in range(len(alist) - 1, 0, -1):
        ofMaxIndex = i
        for j in range(i):
            if alist[ofMaxIndex] < alist[j]:
                ofMaxIndex = j

        alist[i], alist[ofMaxIndex] = alist[ofMaxIndex], alist[i]


def insertSort(alist):
    for i in range(1, len(alist)):
        index = i
        current = alist[i]
        while index > 0 and alist[index - 1] < current:
            alist[index] = alist[index - 1]
            index -= 1

        alist[i] = alist[index]


def shellSort(alist):
    sub = len(alist) // 2
    while sub > 0:
        for start in range(sub):
            for i in range(start + sub, len(alist), sub):
                current = alist[i]
                index = i
                while index > 0 and alist[index - sub] < current:
                    alist[index] = alist[index - sub]
                    index -= sub

                alist[i] = alist[index]


        sub //= 2


def mergeSort(alist):
    if len(alist) > 0:
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

if __name__ == '__main__':
    data = [3, 6, 1, 2, 5, 9, 7, 4]
    bubbleSort(data)
    print(data)
