# Weave Sort - O(n log n)
# Interleaves two sorted halves like weaving cloth threads.
# Split array in half, sort each half, then weave elements together
# taking the smaller one each time (effectively merge sort with visual metaphor).
# Stable | O(n) memory | Alternative name for bottom-up merge sort

from data import *

def weave_sort(lista):
    lst = lista.copy()
    n = len(lst)

    def weave(left, right):
        # weave two sorted arrays together
        result = []
        i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        result.extend(left[i:])
        result.extend(right[j:])
        return result

    # bottom-up: start with threads of size 1, double each pass
    size = 1
    while size < n:
        new_lst = []
        for i in range(0, n, 2 * size):
            left  = lst[i:i + size]
            right = lst[i + size:i + 2 * size]
            new_lst.extend(weave(left, right))
        lst = new_lst
        size *= 2
    return lst[:n]

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(weave_sort(t))
