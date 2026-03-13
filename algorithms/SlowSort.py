# Slow Sort - O(n^(log n / log log n)) — deliberately the slowest correct sort
# "Multiply and surrender" principle — the opposite of divide and conquer.
# Sorts first 2/3, last 2/3, first 2/3 again... recursively.
# Mathematically correct, but designed to be as slow as possible.
# WARNING: do not use on lists with > 15 elements

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
