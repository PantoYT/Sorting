# Quick Sort - O(n log n) avg, O(n²) worst
# Chooses a pivot, moves smaller elements left and larger right,
# then recursively sorts both parts.
# Unstable | In-place | Jeden z najszybszych w praktyce

from data import *

def quick_sort(lista):
    lst = lista.copy()
    if len(lst) <= 1:
        return lst
    pivot = lst[len(lst) // 2]
    left   = [x for x in lst if x < pivot]
    middle = [x for x in lst if x == pivot]
    right  = [x for x in lst if x > pivot]
    return quick_sort(left) + middle + quick_sort(right)

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(quick_sort(t))
