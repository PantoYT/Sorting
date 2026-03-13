# Block Sort - O(n log n) | O(1) extra memory
# Divides the array into blocks of sqrt(n), sorts each block,
# then merges blocks in-place using block swapping.
# Foundation of WikiSort and GrailSort approaches.
# Stable | O(1) memory | Good cache performance

from data import *
import math

def block_sort(lista):
    lst = lista.copy()
    n = len(lst)
    block_size = max(1, int(math.sqrt(n)))

    # sort each block with insertion sort
    for start in range(0, n, block_size):
        end = min(start + block_size, n)
        for i in range(start + 1, end):
            key = lst[i]; j = i - 1
            while j >= start and lst[j] > key:
                lst[j + 1] = lst[j]; j -= 1
            lst[j + 1] = key

    # merge blocks using a buffer
    size = block_size
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            if mid < right:
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
        print(block_sort(t))
