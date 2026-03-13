# Comb Sort - O(n log n) avg
# Improved Bubble Sort — instead of comparing adjacent elements,
# compares elements separated by a gap, shrinks gap each pass (factor 1.3).
# Unstable | In-place | Eliminates "turtles" faster than BubbleSort

from data import *

def comb_sort(lista):
    lst = lista.copy()
    n = len(lst)
    gap = n
    shrink = 1.3
    swapped = True
    while gap > 1 or swapped:
        gap = max(1, int(gap / shrink))
        swapped = False
        for i in range(n - gap):
            if lst[i] > lst[i + gap]:
                lst[i], lst[i + gap] = lst[i + gap], lst[i]
                swapped = True
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(comb_sort(t))
