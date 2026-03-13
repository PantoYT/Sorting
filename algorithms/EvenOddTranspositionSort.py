# Even-Odd Transposition Sort - O(n²) | Parallel-friendly
# Network sort designed for parallel processors.
# Same as OddEvenSort but named differently in parallel computing literature.
# Phase 1 (even): compare (0,1), (2,3), (4,5)...
# Phase 2 (odd):  compare (1,2), (3,4), (5,6)...
# Stable | In-place | Designed for SIMD/parallel execution

from data import *

def even_odd_transposition_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for phase in range(n):
        start = phase % 2  # alternate between 0 (even phase) and 1 (odd phase)
        for i in range(start, n - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(even_odd_transposition_sort(t))
