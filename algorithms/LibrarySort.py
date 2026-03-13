# Library Sort - O(n log n) avg
# InsertionSort with gaps between elements so shifting is faster.
# Like a librarian leaving gaps on the shelf for new books.
# Stable | O(n) memory

from data import *

def library_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    # we use a simple sorted buffer with gaps
    # buffer size = 2*n to leave room for gaps
    GAP_FACTOR = 2
    buf_size = n * GAP_FACTOR
    buf = [None] * buf_size

    # insert first element at position 1 (leave a gap at the start)
    buf[1] = lst[0]
    inserted = 1

    for i in range(1, n):
        x = lst[i]
        # binary search in the buffer (occupied positions only)
        filled = [v for v in buf if v is not None]
        filled.sort()
        # find insertion point via binary search
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
