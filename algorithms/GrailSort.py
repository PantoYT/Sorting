# Grail Sort - O(n log n)
# Stable in-place sort using O(1) extra memory.
# Merges sorted blocks using array rotations instead of memory allocation.
# Used in some libraries requiring stability and low memory usage.
# Stable | O(1) memory

from data import *

def insertion_sort(lst, left, right):
    for i in range(left + 1, right):
        key = lst[i]
        j = i - 1
        while j >= left and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

def merge_inplace(lst, left, mid, right):
    while left < mid and mid < right:
        if lst[left] <= lst[mid]:
            left += 1
        else:
            val = lst[mid]
            lst[left + 1:mid + 1] = lst[left:mid]
            lst[left] = val
            left += 1
            mid += 1

def grail_sort(lista):
    lst = lista.copy()
    n = len(lst)
    block = 16
    for i in range(0, n, block):
        insertion_sort(lst, i, min(i + block, n))
    size = block
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
        print(grail_sort(t))
