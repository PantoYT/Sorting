# Slow Sort - O(n^(log n / log log n)) - celowo najwolniejszy poprawny sort
# Zasada "multiply and surrender" - przeciwieństwo divide and conquer.
# Sortuje pierwsze 2/3, ostatnie 2/3, znowu pierwsze 2/3... rekurencyjnie.
# Poprawny matematycznie, ale zaprojektowany żeby być jak najwolniejszy.
# UWAGA: nie używać na listach > 15 elementów

from data import *

def slow_sort(lst, i, j):
    if i >= j:
        return
    mid = (i + j) // 2
    slow_sort(lst, i, mid)
    slow_sort(lst, mid + 1, j)
    if lst[j] < lst[mid]:
        lst[j], lst[mid] = lst[mid], lst[j]
    slow_sort(lst, i, j - 1)

def slow_sort_wrapper(lista):
    lst = lista.copy()
    slow_sort(lst, 0, len(lst) - 1)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, duplikaty]
    for t in testy:
        print(slow_sort_wrapper(t))
