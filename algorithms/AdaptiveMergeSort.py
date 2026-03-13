# Adaptive Merge Sort - O(n log k) | k = number of runs
# Detects existing sorted runs in the input and merges only those.
# Natural merge sort: if input has k sorted runs, runs in O(n log k).
# Best case O(n) when input is already sorted.
# Stable | O(n) memory | Best adaptive sort for pre-sorted data

from data import *
import heapq

def adaptive_merge_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    # detect natural runs
    runs = []
    start = 0
    for i in range(1, n):
        if lst[i] < lst[i - 1]:
            runs.append(lst[start:i])
            start = i
    runs.append(lst[start:])

    # k-way merge of all runs
    heap = []
    iters = [iter(run) for run in runs]
    for i, it in enumerate(iters):
        val = next(it, None)
        if val is not None:
            heapq.heappush(heap, (val, i))

    result = []
    while heap:
        val, i = heapq.heappop(heap)
        result.append(val)
        nxt = next(iters[i], None)
        if nxt is not None:
            heapq.heappush(heap, (nxt, i))
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(adaptive_merge_sort(t))
