# Tim Sort - O(n log n), O(n) for nearly sorted
# Hybrid of Insertion Sort + Merge Sort. Divides into small blocks (RUN=32),
# sorts each with InsertionSort, then merges with MergeSort.
# This is what sorted() and list.sort() use under the hood in Python.
# Stable | O(n) memory | Najlepszy dla realnych danych

from data import *

RUN = 32

def insertion_sort(lst, left, right):
    for i in range(left + 1, right + 1):
        key = lst[i]
        j = i - 1
        while j >= left and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def merge(lst, left, mid, right):
    l, r = lst[left:mid + 1], lst[mid + 1:right + 1]
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

def tim_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(0, n, RUN):
        insertion_sort(lst, i, min(i + RUN - 1, n - 1))
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(lst, left, mid, right)
        size *= 2
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(tim_sort(t))
