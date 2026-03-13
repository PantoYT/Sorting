# Pigeon Sort - O(n + k) - alias/variant of Pigeonhole Sort
# Uses actual pigeon-inspired homing: each element "flies home"
# to its correct position in one pass using counting.
# Named to distinguish from PigeonHoleSort (different implementation).
# Stable | O(n + k) memory | Only for non-negative integers

from data import *

def pigeon_sort(lista):
    lst = lista.copy()
    mn, mx = min(lst), max(lst)
    size = mx - mn + 1
    holes = [0] * size
    for x in lst:
        holes[x - mn] += 1
    result = []
    for i, count in enumerate(holes):
        result.extend([i + mn] * count)
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(pigeon_sort(t))
