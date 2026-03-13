# Burnt Pancake Sort - O(n²)
# Variant of PancakeSort where each "pancake" has one burnt side.
# Each pancake must land with its burnt side facing down.
# Only operation: prefix reversal (and flipping elements).
# Unstable | In-place

from data import *

def flip(lst, k):
    lst[:k + 1] = lst[:k + 1][::-1]

def burnt_pancake_sort(lista):
    lst = [(x, False) for x in lista]
    n = len(lst)
    for size in range(n, 0, -1):
        max_val = max(lst[:size], key=lambda x: x[0])
        max_i = lst[:size].index(max_val)
        if max_i == size - 1 and lst[size - 1][1]:
            continue
        if max_i != 0:
            flip(lst, max_i)
        if not lst[0][1]:
            lst[0] = (lst[0][0], True)
        flip(lst, size - 1)
        lst[size - 1] = (lst[size - 1][0], True)
    return [x[0] for x in lst]

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, duplikaty]
    for t in testy:
        print(burnt_pancake_sort(t))
