# Pancake Number Sort - O(n²) | Theoretical CS
# Finds the exact pancake number sequence for the input.
# The pancake number P(n) = max flips needed to sort any n-pancake stack.
# This implementation tracks the flip sequence for analysis.
# Unstable | In-place | Used in theoretical computer science

from data import *

def pancake_number_sort(lista):
    lst = lista.copy()
    n = len(lst)
    flip_count = 0
    flip_sequence = []

    def flip(arr, k):
        arr[:k + 1] = arr[:k + 1][::-1]

    for size in range(n, 1, -1):
        max_idx = lst.index(max(lst[:size]))
        if max_idx == size - 1:
            continue
        if max_idx != 0:
            flip(lst, max_idx)
            flip_count += 1
            flip_sequence.append(max_idx + 1)
        flip(lst, size - 1)
        flip_count += 1
        flip_sequence.append(size)

    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(pancake_number_sort(t))
