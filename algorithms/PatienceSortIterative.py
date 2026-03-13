# Iterative Patience Sort - O(n log n)
# Iterative (non-recursive) version of PatienceSort.
# Uses explicit stack/queue management instead of recursion.
# Same algorithm as PatienceSort but without function call overhead.
# Stable | O(n) memory | Slightly faster than recursive due to no call overhead

from data import *
import heapq
import bisect

def patience_sort_iterative(lista):
    lst = lista.copy()
    if len(lst) <= 1:
        return lst

    piles = []
    pile_tops = []

    # deal cards to piles (iterative)
    for x in lst:
        pos = bisect.bisect_left(pile_tops, x)
        if pos < len(piles):
            piles[pos].append(x)
            pile_tops[pos] = x
        else:
            piles.append([x])
            pile_tops.append(x)

    # k-way merge (iterative via heap)
    heap = []
    for i, pile in enumerate(piles):
        heapq.heappush(heap, (pile[-1], i, len(pile) - 1))

    result = []
    pile_ptrs = [len(p) - 1 for p in piles]

    heap = []
    for i, pile in enumerate(piles):
        heapq.heappush(heap, (pile.pop(), i))

    while heap:
        val, i = heapq.heappop(heap)
        result.append(val)
        if piles[i]:
            heapq.heappush(heap, (piles[i].pop(), i))
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(patience_sort_iterative(t))
