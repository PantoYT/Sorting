# Patience Sort - O(n log n)
# Deals elements into piles like solitaire — each card goes to
# the first pile whose top is >= the card. Then merges piles
# using a min-heap. Also finds the Longest Increasing Subsequence (LIS).
# Stable | O(n) memory

from data import *
import heapq

def patience_sort(lista):
    lst = lista.copy()
    piles = []
    for x in lst:
        placed = False
        for pile in piles:
            if pile[-1] >= x:
                pile.append(x)
                placed = True
                break
        if not placed:
            piles.append([x])
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
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(patience_sort(t))
