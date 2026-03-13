# Patience Merge Sort - O(n log n)
# Combines patience solitaire's pile dealing with k-way merge.
# Deals to piles (each pile = descending sequence), reverses piles to get
# ascending runs, then merges all runs with a min-heap.
# Stable | O(n) memory | Naturally adaptive to existing order

from data import *
import heapq

def patience_merge_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    # Phase 1: deal to piles (patience rules: place on leftmost pile whose top >= x)
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

    # Reverse each pile so they become ascending (smallest at index 0)
    for pile in piles:
        pile.reverse()

    # Phase 2: k-way merge using min-heap
    # heap entries: (value, pile_index, position_in_pile)
    heap = []
    for i, pile in enumerate(piles):
        if pile:
            heapq.heappush(heap, (pile[0], i, 0))

    result = []
    while heap:
        val, pi, pos = heapq.heappop(heap)
        result.append(val)
        next_pos = pos + 1
        if next_pos < len(piles[pi]):
            heapq.heappush(heap, (piles[pi][next_pos], pi, next_pos))

    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        ok = patience_merge_sort(t) == sorted(t)
        print(f"OK: {ok}", patience_merge_sort(t))
