# Iterative Merge Sort - O(n log n) | No recursion
# Bottom-up merge sort: starts with sorted subarrays of size 1,
# merges pairs into size 2, then 4, 8, 16... until fully sorted.
# No recursion = no stack overflow on large arrays.
# Stable | O(n) memory | Stack-safe version of MergeSort

from data import *

def iterative_merge_sort(lista):
    lst = lista.copy()
    n = len(lst)
    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            mid   = min(left + size, n)
            right = min(left + 2 * size, n)
            if mid >= right:
                continue
            l, r = lst[left:mid], lst[mid:right]
            i = j = 0; k = left
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    lst[k] = l[i]; i += 1
                else:
                    lst[k] = r[j]; j += 1
                k += 1
            while i < len(l): lst[k] = l[i]; i += 1; k += 1
            while j < len(r): lst[k] = r[j]; j += 1; k += 1
        size *= 2
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(iterative_merge_sort(t))
