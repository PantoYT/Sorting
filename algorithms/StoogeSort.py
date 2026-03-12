# Stooge Sort - O(n^2.7) - celowo głupi rekurencyjny sort
# Sortuje pierwsze 2/3, potem ostatnie 2/3, potem znowu pierwsze 2/3.
# Wolniejszy od większości algorytmów O(n²), ale poprawny.
# UWAGA: nie używać na listach > 20 elementów

from data import *

def stooge_sort_helper(lst, i, j):
    if i >= j:
        return
    if lst[i] > lst[j]:
        lst[i], lst[j] = lst[j], lst[i]
    if j - i + 1 > 2:
        t = (j - i + 1) // 3
        stooge_sort_helper(lst, i, j - t)
        stooge_sort_helper(lst, i + t, j)
        stooge_sort_helper(lst, i, j - t)

def stooge_sort(lista):
    lst = lista.copy()
    stooge_sort_helper(lst, 0, len(lst) - 1)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, duplikaty]
    for t in testy:
        print(stooge_sort(t))
