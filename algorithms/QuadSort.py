# Quad Sort - O(n log n)
# Adaptive sort that first sorts 4-element blocks (quads)
# using sorting networks (fixed number of comparisons), then merges.
# Stable | O(n) memory | Very fast on nearly-sorted data

from data import *

def swap_if_needed(lst, i, j):
    if lst[i] > lst[j]:
        lst[i], lst[j] = lst[j], lst[i]

def sort_quad(lst, i):
    # sorting network for 4 elements — 5 comparisons
    swap_if_needed(lst, i,     i + 1)
    swap_if_needed(lst, i + 2, i + 3)
    swap_if_needed(lst, i,     i + 2)
    swap_if_needed(lst, i + 1, i + 3)
    swap_if_needed(lst, i + 1, i + 2)

def sort_triple(lst, i):
    swap_if_needed(lst, i,     i + 1)
    swap_if_needed(lst, i + 1, i + 2)
    swap_if_needed(lst, i,     i + 1)

def merge(lst, left, mid, right):
    l, r = lst[left:mid], lst[mid:right]
    i = j = 0
    k = left
    while i < len(l) and j < len(r):
        if l[i] <= r[j]:
            lst[k] = l[i]; i += 1
        else:
            lst[k] = r[j]; j += 1
        k += 1
    while i < len(l):
        lst[k] = l[i]; i += 1; k += 1
    while j < len(r):
        lst[k] = r[j]; j += 1; k += 1

def quad_sort(lista):
    lst = lista.copy()
    n = len(lst)
    # posortuj bloki po 4
    i = 0
    while i + 3 < n:
        sort_quad(lst, i)
        i += 4
    # handle remainder (1, 2, or 3 elements)
    rem = n - i
    if rem == 2:
        swap_if_needed(lst, i, i + 1)
    elif rem == 3:
        sort_triple(lst, i)
    # merge with growing block sizes
    size = 4
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            if mid < right:
                merge(lst, left, mid, right)
        size *= 2
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(quad_sort(t) == sorted(t), quad_sort(t))
