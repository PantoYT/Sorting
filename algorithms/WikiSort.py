# Wiki Sort (Block Merge Sort) - O(n log n)
# Stabilny merge sort używający O(1) dodatkowej pamięci.
# Scala bloki przez rotacje in-place zamiast alokowania nowych tablic.
# Stabilny | O(1) pamięci | Kompromis między GrailSort a TimSort

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

def merge_inplace(lst, left, mid, right):
    if left >= mid or mid >= right:
        return
    if mid - left <= right - mid:
        i = left
        while i < mid:
            if lst[i] > lst[mid]:
                lst[i], lst[mid] = lst[mid], lst[i]
                j = mid
                while j < right - 1 and lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]
                    j += 1
            i += 1
    else:
        j = right - 1
        while j >= mid:
            if lst[mid - 1] > lst[j]:
                lst[mid - 1], lst[j] = lst[j], lst[mid - 1]
                i = mid - 1
                while i > left and lst[i - 1] > lst[i]:
                    lst[i - 1], lst[i] = lst[i], lst[i - 1]
                    i -= 1
            j -= 1

def wiki_sort(lista):
    lst = lista.copy()
    n = len(lst)
    block_size = max(1, int(math.sqrt(n)))
    for i in range(0, n, block_size):
        insertion_sort(lst, i, min(i + block_size - 1, n - 1))
    size = block_size
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            if mid < right:
                merge_inplace(lst, left, mid, right)
        size *= 2
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(wiki_sort(t))
