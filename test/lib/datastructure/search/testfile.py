from lib.datastructure.search import binarySearch, sequenceSearch, HashTable

import random
import pytest


class TestSearch:
    test_data = [random.randint(0, 10) for _ in range(10)]

    @pytest.mark.parametrize(
        'search', [
            binarySearch,
            sequenceSearch
        ]
    )
    def test_search(self, search):
        print(f"\nTEST SEARCH {search.__name__}\n")
        print(f"test_data: {self.test_data}")
        for i in range(10):
            print(f"test find {i} in test_data, result is {search(self.test_data, i)}")

    def test_hash(self):
        print("\nTEST HASH TABLE\n")

        H = HashTable()

        for i in range(10):
            H[i] = i * 2
            print(f"test put key and value\n, result is key = {i}, val = {H[i]}")
            print("\n")

        print("test add size")
        print(len(H))
        pos = len(H)
        j = 0
        for i in range(100):
            H[i] = i * 2
            if len(H) != pos:
                print(f"add time {j}", len(H))
                j += 1
                pos = len(H)
                H.show()

        H.Init()
        print(f"Init later Size = {len(H)}")
        H.show()
