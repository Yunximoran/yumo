from lib.datastructure.list.order import OrderList
from lib.datastructure.list.unordered import UnorderedList

import pytest
import random
import sys
import os

from datetime import datetime

outfile = "output"

if not os.path.exists(outfile):
    os.mkdir(outfile)


# 增删查通过
#

@pytest.mark.parametrize(
    "link", [
        (OrderList()),
        (UnorderedList())
    ]
)
def test_link(link):
    # f = open(f'output/{link}.txt', 'a')
    # sys.stdout = f
    print(f"\nTEST LINK {link} TIME:[ - {datetime.now()} - ]\n")
    test_vals = None
    if isinstance(link, UnorderedList):
        test_vals = [i for i in range(10)]

    if isinstance(link, OrderList):
        test_vals = [random.randint(0, 10) for _ in range(10)]

    for val in test_vals:
        link.addNode(val)
        print(f"success addNode {val}, now {link} len = ", len(link))

    print(f"test {link} findNode: 2, result is ", link.findNode(2))
    print(f"test {link} findNode: 3, result is ", link.findNode(3))
    print(f"test {link} findNode: 4, result is ", link.findNode(4))

    link.removeNode(2)
    link.removeNode(3)
    link.removeNode(4)
    print(f"success removeNode all now {link} len = {len(link)}")

    print(f"test {link} contains func, result: ", (2 in link))  # False
    print(f"test {link} contains func, result: ", (3 in link))  # False
    print(f"test {link} contains func, result: ", (5 in link))  # if ul True else True | False

    for i, val in enumerate(link):
        print(f"test {link} iter func, index: {i} - result: {val}")

    # sys.stdout = sys.__stdout__
    # f.close()
