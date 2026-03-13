# Ternary Split Quick Sort - O(n log n) | Best on data with many duplicates
# Uses Dutch National Flag partitioning (3-way split):
# elements < pivot | elements == pivot | elements > pivot
# Runs in O(n) time when all elements are equal.
# Unstable | In-place | Also known as "fat pivot" partitioning

from data import *
import random

def ternary_split_quick_sort(lista):
    lst = lista.copy()

    def _sort(arr, lo, hi):
        if lo >= hi:
            return
        pivot = arr[random.randint(lo, hi)]
        lt, gt = lo, hi
        i = lo
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]; lt += 1; i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]; gt -= 1
            else:
                i += 1
        _sort(arr, lo, lt - 1)
        _sort(arr, gt + 1, hi)

    _sort(lst, 0, len(lst) - 1)
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(ternary_split_quick_sort(t))
