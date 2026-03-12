# Library Sort - O(n log n) avg
# InsertionSort z lukami między elementami żeby przesuwanie było szybsze.
# Jak bibliotekarz zostawiający wolne miejsca na półce na nowe książki.
# Stabilny | O(n) pamięci

from data import *

def library_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    # używamy zwykłego posortowanego bufora z lukami
    # rozmiar bufora = 2*n żeby było dość miejsca na luki
    GAP_FACTOR = 2
    buf_size = n * GAP_FACTOR
    buf = [None] * buf_size

    # wstaw pierwszy element na pozycję 1 (zostaw lukę na początku)
    buf[1] = lst[0]
    inserted = 1

    for i in range(1, n):
        x = lst[i]
        # binary search w buforze (tylko na zajętych pozycjach)
        filled = [v for v in buf if v is not None]
        filled.sort()
        # znajdź gdzie wstawić przez binary search
        lo, hi = 0, len(filled)
        while lo < hi:
            mid = (lo + hi) // 2
            if filled[mid] < x:
                lo = mid + 1
            else:
                hi = mid
        filled.insert(lo, x)
        inserted += 1

        # przepisz posortowane z lukami
        buf = [None] * buf_size
        step = buf_size // (inserted + 1)
        for j, val in enumerate(filled):
            pos = (j + 1) * step
            if pos < buf_size:
                buf[pos] = val

    return [v for v in buf if v is not None]

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty]
    for t in testy:
        print(library_sort(t) == sorted(t), library_sort(t))
