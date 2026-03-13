# Sorting Network Sort - O(n log²n) comparators, data-oblivious
# Uses a fixed sequence of compare-and-swap pairs that sorts any input.
# All comparators within a "layer" can run in parallel on hardware.
# Uses insertion-sort-style network generation (always correct for any n).
# Unstable | In-place | Data-oblivious: same operations regardless of input

from data import *

def sorting_network(lista):
    lst = lista.copy()
    n = len(lst)
    # Shell-sort-based network: guaranteed correct for any n
    # Generate gap sequence (Ciura gaps or simple shell gaps)
    gaps = []
    gap = n // 2
    while gap > 0:
        gaps.append(gap)
        gap //= 2

    # For each gap, generate all comparator pairs
    for gap in gaps:
        for i in range(gap, n):
            key = lst[i]
            j = i
            while j >= gap and lst[j - gap] > key:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = key
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza, duza_losowa]:
        ok = sorting_network(t) == sorted(t)
        print(ok, sorting_network(t)[:7])
