# Funnel Sort - O(n log²n / B) cache-efficient
# Cache-oblivious algorithm: uses a recursive "funnel" structure
# to achieve optimal cache performance without knowing cache size.
# Each funnel merges sorted sequences through a binary tree of buffers.
# Implementation here uses simplified funnel merge structure.
# Stable | O(n log n) memory | Optimal cache performance

from data import *

def funnel_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    def _sort(arr):
        if len(arr) <= 8:
            # base case: insertion sort
            for i in range(1, len(arr)):
                key = arr[i]; j = i - 1
                while j >= 0 and arr[j] > key:
                    arr[j + 1] = arr[j]; j -= 1
                arr[j + 1] = key
            return arr
        # split into k = sqrt(n) segments
        import math
        k = max(2, int(math.sqrt(len(arr))))
        seg_size = (len(arr) + k - 1) // k
        segments = []
        for i in range(0, len(arr), seg_size):
            segments.append(_sort(arr[i:i + seg_size]))
        # k-way merge through funnel structure
        import heapq
        heap = []
        iters = [iter(s) for s in segments]
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

    return _sort(lst)

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(funnel_sort(t))
