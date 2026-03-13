# Dual Pivot Quick Sort - O(n log n) | Java Arrays.sort() for primitives
# Uses TWO pivots instead of one, creating three partitions:
# elements < pivot1 | pivot1 <= elements <= pivot2 | elements > pivot2
# In practice 10-15% faster than single-pivot QuickSort.
# This is the algorithm used in Java's Arrays.sort() for primitive types.
# Unstable | In-place | Industry standard since Java 7

from data import *

def dual_pivot_quick_sort(lista):
    lst = lista.copy()

    def _sort(arr, lo, hi):
        if lo >= hi:
            return
        if arr[lo] > arr[hi]:
            arr[lo], arr[hi] = arr[hi], arr[lo]
        p1, p2 = arr[lo], arr[hi]
        lt, gt = lo + 1, hi - 1
        i = lo + 1
        while i <= gt:
            if arr[i] < p1:
                arr[i], arr[lt] = arr[lt], arr[i]; lt += 1; i += 1
            elif arr[i] > p2:
                arr[i], arr[gt] = arr[gt], arr[i]; gt -= 1
            else:
                i += 1
        lt -= 1; gt += 1
        arr[lo], arr[lt] = arr[lt], arr[lo]
        arr[hi], arr[gt] = arr[gt], arr[hi]
        _sort(arr, lo, lt - 1)
        _sort(arr, lt + 1, gt - 1)
        _sort(arr, gt + 1, hi)

    _sort(lst, 0, len(lst) - 1)
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(dual_pivot_quick_sort(t))
