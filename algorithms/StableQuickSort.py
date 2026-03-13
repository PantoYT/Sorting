# Stable Quick Sort - O(n log n) | Stable version of QuickSort
# Partitions into three lists (less, equal, greater) instead of in-place swaps.
# This makes it stable: equal elements maintain their original relative order.
# Stable | O(n) memory | Trade-off: uses more memory than in-place QuickSort

from data import *

def stable_quick_sort(lista):
    lst = lista.copy()

    def _sort(arr):
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]
        less    = [x for x in arr if x < pivot]
        equal   = [x for x in arr if x == pivot]
        greater = [x for x in arr if x > pivot]
        return _sort(less) + equal + _sort(greater)

    return _sort(lst)

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(stable_quick_sort(t))
