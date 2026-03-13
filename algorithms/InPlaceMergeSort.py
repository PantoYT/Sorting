# In-Place Merge Sort - O(n log²n) | O(1) extra memory
# Merge sort that merges in-place using rotation instead of buffer.
# Sacrifices O(log n) time factor to achieve O(1) extra memory.
# Stable | O(log n) stack | Memory-constrained environments

from data import *

def in_place_merge_sort(lista):
    lst = lista.copy()

    def rotate(arr, lo, mid, hi):
        # rotate arr[lo:hi] such that arr[mid:hi] comes before arr[lo:mid]
        arr[lo:hi] = arr[mid:hi] + arr[lo:mid]

    def merge(arr, lo, mid, hi):
        i, j = lo, mid
        while i < j and j < hi:
            if arr[i] <= arr[j]:
                i += 1
            else:
                val = arr[j]
                arr[i + 1:j + 1] = arr[i:j]
                arr[i] = val
                i += 1; j += 1

    def sort(arr, lo, hi):
        if hi - lo <= 1:
            return
        mid = (lo + hi) // 2
        sort(arr, lo, mid)
        sort(arr, mid, hi)
        merge(arr, lo, mid, hi)

    sort(lst, 0, len(lst))
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(in_place_merge_sort(t))
