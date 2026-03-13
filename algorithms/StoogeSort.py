# Stooge Sort - O(n^2.7) — deliberately stupid recursive sort
# Sorts first 2/3, then last 2/3, then first 2/3 again.
# Slower than most O(n²) algorithms, but correct.
# WARNING: do not use on lists with > 20 elements

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
