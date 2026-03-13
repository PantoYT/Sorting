# Optimized Patience Sort - O(n log n)
# Improvement over basic PatienceSort using binary search to find
# the correct pile instead of linear scan.
# Also finds the Longest Increasing Subsequence (LIS) as a side effect.
# Stable | O(n) memory | The binary search makes pile placement O(log n)

from data import *
import heapq
import bisect

def patience_opt_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    piles = []       # list of piles (each pile = list, top accessible)
    pile_tops = []   # just the tops for binary search

    for x in lst:
        # binary search for leftmost pile whose top >= x
        pos = bisect.bisect_left(pile_tops, x)
        if pos == len(piles):
            piles.append([x])
            pile_tops.append(x)
        else:
            piles[pos].append(x)
            pile_tops[pos] = x

    # k-way merge using heap
    heap = []
    for i, pile in enumerate(piles):
        heapq.heappush(heap, (pile.pop(), i))

    result = []
    while heap:
        val, i = heapq.heappop(heap)
        result.append(val)
        if piles[i]:
            heapq.heappush(heap, (piles[i].pop(), i))
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(patience_opt_sort(t))
