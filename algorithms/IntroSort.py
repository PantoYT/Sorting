# Intro Sort - O(n log n)
# Hybrid of QuickSort + HeapSort + InsertionSort.
# Starts with QuickSort; if recursion goes too deep, switches to HeapSort;
# for small arrays (< 16) uses InsertionSort.
# This is std::sort in C++.
# Unstable | In-place | Bardzo szybki w praktyce

from data import *
import math

def insertion_sort(lst, left, right):
    for i in range(left + 1, right + 1):
        key = lst[i]
        j = i - 1
        while j >= left and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def heapify(lst, n, i, left):
    largest = i
    l = 2 * (i - left) + 1 + left
    r = 2 * (i - left) + 2 + left
    if l <= left + n - 1 and lst[l] > lst[largest]:
        largest = l
    if r <= left + n - 1 and lst[r] > lst[largest]:
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest, left)

def heap_sort(lst, left, right):
    n = right - left + 1
    for i in range(left + n // 2 - 1, left - 1, -1):
        heapify(lst, n, i, left)
    for i in range(right, left, -1):
        lst[left], lst[i] = lst[i], lst[left]
        heapify(lst, i - left, left, left)

def partition(lst, low, high):
    pivot = lst[high]
    i = low - 1
    for j in range(low, high):
        if lst[j] <= pivot:
            i += 1
            lst[i], lst[j] = lst[j], lst[i]
    lst[i + 1], lst[high] = lst[high], lst[i + 1]
    return i + 1

def introsort_helper(lst, low, high, depth_limit):
    if high - low + 1 < 16:
        insertion_sort(lst, low, high)
        return
    if depth_limit == 0:
        heap_sort(lst, low, high)
        return
    pivot = partition(lst, low, high)
    introsort_helper(lst, low, pivot - 1, depth_limit - 1)
    introsort_helper(lst, pivot + 1, high, depth_limit - 1)

def intro_sort(lista):
    lst = lista.copy()
    n = len(lst)
    depth_limit = 2 * math.floor(math.log2(n)) if n > 1 else 0
    introsort_helper(lst, 0, n - 1, depth_limit)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(intro_sort(t))
