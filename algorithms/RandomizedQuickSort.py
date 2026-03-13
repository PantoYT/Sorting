# Randomized Quick Sort - O(n log n) expected, O(n²) worst case
# QuickSort with random pivot selection to avoid worst-case O(n²)
# on sorted/nearly-sorted inputs.
# Expected O(n log n) regardless of input distribution.
# Unstable | In-place | Industry standard improvement over basic QuickSort

from data import *
import random

def randomized_quick_sort(lista):
    lst = lista.copy()

    def _sort(arr, lo, hi):
        if lo >= hi:
            return
        # random pivot
        pivot_idx = random.randint(lo, hi)
        arr[pivot_idx], arr[hi] = arr[hi], arr[pivot_idx]
        pivot = arr[hi]
        i = lo - 1
        for j in range(lo, hi):
            if arr[j] <= pivot:
                i += 1
                arr[i], arr[j] = arr[j], arr[i]
        arr[i + 1], arr[hi] = arr[hi], arr[i + 1]
        p = i + 1
        _sort(arr, lo, p - 1)
        _sort(arr, p + 1, hi)

    _sort(lst, 0, len(lst) - 1)
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(randomized_quick_sort(t))
