# Bitonic Merge Sort - O(n log²n) | Great for parallel hardware
# Variant of BitonicSort using explicit merge network.
# Builds bitonic sequences bottom-up, merges them using comparator networks.
# Well-suited for GPU implementation (all comparisons independent).
# Unstable | In-place | Works on power-of-2 sizes (pads with inf)

from data import *
import math

def bitonic_merge_sort(lista):
    lst = lista.copy()
    n = len(lst)
    size = 2 ** math.ceil(math.log2(n)) if n > 1 else 1
    lst += [float('inf')] * (size - n)

    def compare_swap(arr, i, j, asc):
        if (arr[i] > arr[j]) == asc:
            arr[i], arr[j] = arr[j], arr[i]

    def bitonic_merge(arr, lo, cnt, asc):
        if cnt > 1:
            k = cnt // 2
            for i in range(lo, lo + k):
                compare_swap(arr, i, i + k, asc)
            bitonic_merge(arr, lo, k, asc)
            bitonic_merge(arr, lo + k, k, asc)

    def bitonic_sort_rec(arr, lo, cnt, asc):
        if cnt > 1:
            k = cnt // 2
            bitonic_sort_rec(arr, lo, k, True)
            bitonic_sort_rec(arr, lo + k, k, False)
            bitonic_merge(arr, lo, cnt, asc)

    bitonic_sort_rec(lst, 0, size, True)
    return lst[:n]

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(bitonic_merge_sort(t))
