def bubbleSort(alist):  # 冒泡排序
    for passnum in range(len(alist) - 1, 0, -1):
        for i in range(passnum):
            if alist[i] > alist[i + 1]:
                alist[i], alist[i + 1] = alist[i + 1], alist[i]
            # if alist[passnum] > alist[i]:
            #     alist[passnum], alist[i] = alist[i], alist[passnum]
            # 两种方法都能实现排序 ？？？


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
    # 在alist中找到最大值，将其与末位元素交换
    for fillslot in range(len(alist) - 1, 0, -1):
        positionOfMax = 0
        for location in range(1, fillslot + 1):
            if alist[location] > alist[positionOfMax]:
                positionOfMax = location

        alist[fillslot], alist[positionOfMax] = alist[positionOfMax], alist[fillslot]


def insertSort(alist):
    # 第一层循环从第二个元素开始遍历
    for index in range(1, len(alist)):
        currentvalue = alist[index]  # 获取当前值
        position = index  # 获取当前索引

        while position > 0 and alist[position - 1] > currentvalue:  # 如果alist[position] < currentvalue 说明需要交换
            alist[position] = alist[position - 1]  #
            position = position - 1

        alist[position] = currentvalue
    """
    [5, 2, 6, 4, 3, 1]
    
    step 1: [5, 2] [6, 4, 3, 1], currentvalue = 2
    
        while position > 0 and alist[position - 1] > currentvalue:
            position = 1, alist[0] = 5: alist[1] = alist[0] = 5, alist: [5, 5], (position = 0)
            position = 0, alist[0] = 5: break
        
        alist[0] = 2, alist: [2, 5]
    
    step 2: [2, 5, 6] [4, 3, 1], currentvalue = 6
    
        while position > 0 and alist[position - 1] > currentvalue:
            position = 2, alist[1] = 5: break
        
        alist[2] = 6, alist: [2, 5, 6]
    
    step 3: [2, 5, 6, 4] [3, 1], currentvalue = 4
    
        while position > 0 and alist[position - 1] > currentvalue:
            position = 3, alist[2] = 6: alist[3] = alist[2] = 6, alist[2, 5, 6, 6], (position--)
            position = 2, alist[1] = 5: alist[2] = alist[1] = 5, alist[2, 5, 5, 6], (position--)
            position = 1, alist[0] = 2: break
        
        alist[1] = 4, alist: [2, 4, 5, 6]
    
    
    step 4: [2, 4, 5, 6, 3] [1], currentvalue = 3
    
        while position > 0 and alist[position - 1] > currentvalue:
            position = 4, alist[3] = 6: alist[4] = alist[3] = 5, alist: [2, 4, 5, 6, 6], (position--)
            position = 3, alist[2] = 5: alist[3] = alist[2] = 5, alist: [2, 4, 5, 5, 6], (position--)
            position = 2, alist[1] = 4: alist[2] = alist[1] = 4, alist: [2, 4, 4, 5, 6], (position--)
            position = 1, alist[0] = 2: break
        
        alist[1] = 3, alist: [2, 3, 4, 5, 6]


    step 5: [2, 3, 4, 5, 6, 1] [], currentvalue = 1
    
        while position > 0 and alist[position - 1] > currentvalue:
            position = 5, alist[4] = 6: alist[5] = alist[4] = 6, alist: [2, 3, 4, 5, 6, 6], (position--)
            position = 4, alist[3] = 5: alist[4] = alist[3] = 5, alist: [2, 3, 4, 5, 5, 6], (position--)
            position = 3, alist[2] = 4: alist[3] = alist[2] = 4, alist: [2, 3, 4, 4, 5, 6], (position--)
            position = 2, alist[1] = 3: alist[2] = alist[1] = 3, alist: [2, 3, 3, 4, 5, 6], (position--)
            position = 1, alist[0] = 2: alist[1] = alist[0] = 2, alist: [2, 2, 3, 4, 5, 6], (position--)
            position = 0: break
        
        alist[0] = 1, alist: [1, 2, 3, 4, 5, 6]
    
    """


def shellSort(alist):
    sublistcount = len(alist) // 2
    while sublistcount > 0:
        for startposition in range(sublistcount):
            gapInsertionSort(alist, startposition, sublistcount)

        print("After increments of size", sublistcount, "The list is", alist)
        sublistcount //= 2





def gapInsertionSort(alist, start, gap):
    for i in range(start + gap, len(alist), gap):
        currentvalue = alist[i]
        position = i
        while position > gap and alist[position - gap] > currentvalue:
            alist[position] = alist[position - gap]
            position -= gap

        alist[position] = currentvalue


def mergeSort(alist):
    print("Splitting ", alist)
    # 归并排序， 将列表切分成两部分，分别由lefthalf 和 righthalf 接受并记录
    # 然后对原列表进行重写
    if len(alist) > 1:
        mid = len(alist) // 2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        # 将原列表切分为左右两部分，分别由两个变量记录

        # 递归，当列表中元素只剩两个时，进入排序
        mergeSort(lefthalf)  # 切分列表
        mergeSort(righthalf)

        i = 0
        j = 0
        k = 0
        print(f"alist: {alist}, left: {lefthalf}, right: {righthalf}")
        while i < len(lefthalf) and j < len(righthalf):
            # i 和 j 的变化并不同步
            # 1.分别取出 left 和 right 的第一个值进行比较
            # 2.如果 left[0] > right[0] 则 left[0] 继续比较 right[1]
            """ * left 与 right 必须各自有序
            
            保证: 如果 left[0] > right[0], 则必须有 left[1] > right[0]
            
            这样做的目的是 保证每次将元素写入 alist 时， 该元素一定是所有[未访问 元素]中的最小值，[已访问 元素]中的最大值
            """
            # 3.每次比较都将较小值， 从0开始，顺序写入 alist
            # 这部分循环结束时，可以保证 alist 前半部分是有序地
            if lefthalf[i] < righthalf[j]:
                print(f"alist[{k}] = {lefthalf[i]}", end=" ")
                alist[k] = lefthalf[i]
                i += 1
            else:
                print(f"alist[{k}] = {righthalf[j]}", end=" ")
                alist[k] = righthalf[j]
                j += 1
            print(f"i = {i}, j = {j}, k = {k}  -> alist: {alist}")
            k += 1

        # 执行完第一个循环后，left 和 right 一定有一个被完全访问并排序
        # 而另一个 left[right] 中， i[j] 索引的值一定是，[已访问 元素] 中的最大值
        # 因为 left 与 right 各自有序， 所以需要将 left[right]中剩下未被访问元素 逐个写入 alist 即可
        while i < len(lefthalf):
            print(f"alist[{k}] = {lefthalf[i]}", end=" ")
            alist[k] = lefthalf[i]
            i += 1
            k += 1
            print(f"i = {i}, k = {k} -> alist: {alist}")

        while j < len(righthalf):
            print(f"alist[{k}] = {righthalf[j]}", end=" ")
            alist[k] = righthalf[j]
            j += 1
            k += 1
            print(f"j = {j}, k = {k} -> alist: {alist}")

        # 这个过程中 alist 的索引 k 会在每次执行操作时 累加
        # 即：
        print("Merging", alist)

    """
    [5, 2, 6, 4, 3, 1]
    |   [5, 2, 6]
    |   |   [5] -> return [2]
    |   |   [2, 6]
    |   |   |   [2] -> return [2]
    |   |   |   [6] -> return [6]
    |   |   |           
    |   |   |   step: alist: [2, 6], left: [2], right: [6]
    |   |   |
    |   |   |   while i < len([2]) and j < len([6])
    |   |   |       i = 0, j = 0, k = 0: [2] < [6], alist[0] = 2, alist: [2, 6], (i++, k++)
    |   |   |       i = 1, j = 0, k = 1: break
    |   |   |       
    |   |   |   while i < len([2]):
    |   |   |       i = 1, k = 1: break
    |   |   |          
    |   |   |   while j < len([6]):
    |   |   |       j = 0, k = 1: alist[1] = 6, alist: [2, 6], (j++, k++)
    |   |   |       j = 1, k = 2: break
    |   |   |           
    |   |   |-> return [2, 6]
    |   |   
    |   |   step: alist: [5, 2, 6], left:[5], right: [2, 6]
    |   |
    |   |   while i < len([5]) and j < len([2, 6]):
    |   |       i = 0, j = 0, k = 0: [5] > [2], alist[0] = 2, alist: [2, 2, 6], (j++, k++)
    |   |       i = 0, j = 1, k = 1: [5] < [6], alist[1] = 5, alist: [2, 5, 6], (i++, k++)
    |   |       i = 1, j = 1, k = 2: break
    |   |
    |   |   while i < len([5]):
    |   |       i = 1, k = 2: break
    |   |   
    |   |   while j < len([2, 6]):
    |   |       j = 1, k = 2: alist[2] = 6, alist: [2, 5, 6], (j++, k++)
    |   |       j = 2, k = 3: break
    |   |   
    |   |-> return [2, 5, 6]
    |   
    |   [4, 3, 1]               
    |   |   [4] -> return [4]
    |   |   [3. 1]          
    |   |   |   [3] -> return [3]
    |   |   |   [1] -> return [1]
    |   |   |
    |   |   |   step: alist: [3, 1], left: [3], right[1]
    |   |   |
    |   |   |   while i < len([3]) and j < len([1]):
    |   |   |       i = 0, j = 0, k = 0: [3] > [1], alist[0] = 1, alist: [1, 1], (j++, k++)
    |   |   |       i = 0, j = 1, k = 1: break
    |   |   |   
    |   |   |   while i < len([3]):
    |   |   |       i = 0, k = 1: alist[1] = 3, alist: [1, 3]
    |   |   |   
    |   |   |   while j < len([1]):
    |   |   |       j = 1, k = 2: break
    |   |   |   
    |   |   |-> return [1, 3]
    |   |   
    |   |   step: left: [4], right: [1, 3]
    |   |
    |   |   while i < len([4]) and j < len([1, 3])
    |   |       i = 0, j = 0, k = 0: [4] > [1], alist[0] = 1, alist[1, 3, 1], (j++, k++)
    |   |       i = 0, j = 1, k = 1: [4] > [3], alist[1] = 3, alist[1, 3, 1], (j++, k++)
    |   |       i = 0, j = 2, k = 2: break
    |   |   
    |   |   while i < len([4]):
    |   |       i = 0, k = 2: alist[2] = 4, alist: [1, 3, 4], (i++, k++)
    |   |       i = 1, k = 3: break
    |   |   
    |   |   while j < len([1, 3]):
    |   |       j = 2, k = 3: break
    |   |   
    |   |-> return [1, 3, 4]
    |   
    |   step: alist: [5, 2, 6, 4, 3, 1], left: [2, 5, 6], right: [1, 3, 4]
    |   
    |   while i < len(2, 5, 6) and j < len([1, 3, 4]):
    |       i = 0, j = 0, k = 0: [2] > [1], alist[0] = 1, alist: [1, 2, 6, 4, 3, 1], (j++, k++)
    |       i = 0, j = 1, k = 1: [2] < [3], alist[1] = 2, alist: [1, 2, 6, 4, 3, 1], (i++, k++)
    |       i = 1, j = 1, k = 2: [5] > [3], alist[2] = 3, alist: [1, 2, 3, 4, 3, 1], (j++, k++)
    |       i = 1, j = 2, k = 3: [5] > [4], alist[3] = 4, alist: [1, 2, 3, 4, 3, 1], (j++, k++)
    |       i = 1, j = 3, k = 4: break
    |   
    |   while i < len([2, 5, 6]):
    |       i = 1, k = 4: alist[4] = 5, alist: [1, 2, 3, 4, 5, 1], (i++, k++)
    |       i = 2, k = 5: alist[5] = 6, alist: [1, 2, 3, 4, 5, 6], (i++, k++)
    |       i = 3, k = 6: break
    |   
    |   while j < len([1, 3, 4]):
    |       j = 3, k = 6: break
    |   
    |-> return [1, 2, 3, 4, 5, 6]    
    """


if __name__ == '__main__':
    import random

    alist = [random.randint(0, 10) for x in range(10)]

    shellSort(alist)
    print(alist)
