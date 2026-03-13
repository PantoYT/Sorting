# Bitonic Sort - O(n log²n)
# Builds bitonic sequences (ascending-descending), then merges them.
# Only works correctly for n that is a power of 2 (padded with INF).
# Unstable | In-place | Great for parallel implementations (GPU)

from data import *
import math

def compare_and_swap(lst, i, j, direction):
    if (lst[i] > lst[j]) == direction:
        lst[i], lst[j] = lst[j], lst[i]

def bitonic_merge(lst, low, n, direction):
    if n > 1:
        mid = n // 2
        for i in range(low, low + mid):
            compare_and_swap(lst, i, i + mid, direction)
        bitonic_merge(lst, low, mid, direction)
        bitonic_merge(lst, low + mid, mid, direction)

def bitonic_sort_helper(lst, low, n, direction):
    if n > 1:
        mid = n // 2
        bitonic_sort_helper(lst, low, mid, True)
        bitonic_sort_helper(lst, low + mid, mid, False)
        bitonic_merge(lst, low, n, direction)

def bitonic_sort(lista):
    lst = lista.copy()
    n = len(lst)
    size = 2 ** math.ceil(math.log2(n)) if n > 1 else 1
    lst += [float('inf')] * (size - n)
    bitonic_sort_helper(lst, 0, size, True)
    return lst[:n]

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(bitonic_sort(t))
