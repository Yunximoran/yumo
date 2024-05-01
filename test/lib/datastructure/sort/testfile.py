from lib.datastructure.sort import *

import pytest


@pytest.mark.parametrize(
    "sort", [
        bubbleSort,
        shortBubbleSort,
        selectSort,
        insertSort,
        shellSort,
        mergeSort,
    ]
)
def test_sort(sort):
    print("\nTEST SORT\n")

    alist = [5, 2, 6, 4, 3, 1]

    sort(alist)
    print(f"{sort.__name__} after alist: {alist}")
