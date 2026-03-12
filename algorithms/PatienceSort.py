# Patience Sort - O(n log n)
# Układa elementy w stosy jak w pasjansie - każda karta trafia na
# pierwszy stos gdzie wierzch jest >= karta. Potem scala stosy
# używając min-heap. Przy okazji znajduje najdłuższy rosnący podciąg (LIS).
# Stabilny | O(n) pamięci

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
