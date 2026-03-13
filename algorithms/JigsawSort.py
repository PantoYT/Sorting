# Jigsaw Sort - O(n²)
# Sorts "jigsaw-style" — splits list into pieces, sorts each,
# then merges them like a puzzle matching edges (last element of block <= first of next).
# If pieces don't fit, swaps boundary elements and repeats.
# Stable | O(n) memory | Original educational algorithm

from data import *

def jigsaw_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    block = max(2, n // 4)
    # sortuj bloki
    for i in range(0, n, block):
        end = min(i + block, n)
        lst[i:end] = sorted(lst[i:end])
    # merge by matching "edges" until the whole is sorted
    changed = True
    while changed:
        changed = False
        for i in range(0, n, block):
            end = min(i + block, n)
            next_start = end
            next_end = min(next_start + block, n)
            if next_end <= n and next_start < n:
                if lst[end - 1] > lst[next_start]:
                    segment = lst[i:next_end]
                    segment.sort()
                    lst[i:next_end] = segment
                    changed = True
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(jigsaw_sort(t))
