# Pigeonhole Sort - O(n + k)
# Creates a separate "hole" for each possible value and places elements there.
# Similar to Counting Sort but keeps the actual elements instead of counting.
# Stable | O(n + k) memory | Good when range ≈ number of elements

from data import *

def pigeonhole_sort(lista):
    lst = lista.copy()
    min_val, max_val = min(lst), max(lst)
    holes = [[] for _ in range(max_val - min_val + 1)]
    for x in lst:
        holes[x - min_val].append(x)
    result = []
    for hole in holes:
        result.extend(hole)
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(pigeonhole_sort(t))
