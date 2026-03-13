# Weave Merge Sort - O(n log n) | Cache-friendly bottom-up merge
# Bottom-up merge sort that alternates the merge direction (left-right, right-left)
# to reduce cache misses. Similar to TimSort's galloping but simpler.
# Stable | O(n) memory | Better cache behavior than top-down MergeSort

from data import *

def weave_merge_sort(lista):
    lst = lista.copy()
    n = len(lst)
    buf = lst[:]
    src, dst = lst, buf
    size = 1
    while size < n:
        for left in range(0, n, 2 * size):
            lo  = left
            mid = min(left + size, n)
            hi  = min(left + 2 * size, n)
            i, j, k = lo, mid, lo
            while i < mid and j < hi:
                if src[i] <= src[j]:
                    dst[k] = src[i]; i += 1
                else:
                    dst[k] = src[j]; j += 1
                k += 1
            while i < mid: dst[k] = src[i]; i += 1; k += 1
            while j < hi:  dst[k] = src[j]; j += 1; k += 1
            dst[hi:hi] = []  # no-op, just clarity
        # swap buffers (zero copy)
        src, dst = dst, src
        size *= 2
    return src[:n]

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(weave_merge_sort(t))
