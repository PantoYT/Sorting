# Optimized Pancake Sort - O(n²) with fewer flips than naive PancakeSort
# Uses 2 flips per element instead of potentially many.
# Finds the max, brings it to front (1 flip), then flips to final position (1 flip).
# Guaranteed 2*(n-1) flips maximum for n elements.
# Unstable | In-place | Improved over naive PancakeSort

from data import *

def optimized_pancake_sort(lista):
    lst = lista.copy()
    n = len(lst)

    def flip(arr, k):
        arr[:k + 1] = arr[:k + 1][::-1]

    for size in range(n, 1, -1):
        max_idx = lst.index(max(lst[:size]))
        if max_idx == size - 1:
            continue
        if max_idx != 0:
            flip(lst, max_idx)   # bring max to front
        flip(lst, size - 1)      # flip max to final position
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(optimized_pancake_sort(t))
