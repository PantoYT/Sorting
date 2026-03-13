# Binary Insertion Sort - O(n log n) comparisons, O(n²) swaps
# Insertion sort that uses binary search to find the insertion position.
# Reduces number of comparisons from O(n²) to O(n log n).
# Still O(n²) overall due to element shifting, but fewer comparisons.
# Stable | In-place | Better than InsertionSort when comparisons are expensive

from data import *
import bisect

def binary_insertion_sort(lista):
    lst = lista.copy()
    for i in range(1, len(lst)):
        key = lst[i]
        # binary search for insertion position in sorted portion lst[0:i]
        pos = bisect.bisect_left(lst, key, 0, i)
        # shift elements right to make room
        lst[pos + 1:i + 1] = lst[pos:i]
        lst[pos] = key
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(binary_insertion_sort(t))
