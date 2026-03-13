# Recursive Insertion Sort - O(n²)
# Same as Insertion Sort but implemented recursively.
# Base case: array of size 1 is sorted.
# Recursive case: sort first n-1 elements, then insert n-th element.
# Educational: demonstrates recursion on a simple algorithm.
# Stable | In-place | Stack depth O(n) - not for large arrays

from data import *

def recursive_insertion_sort(lista):
    lst = lista.copy()

    def _insert(arr, n):
        if n <= 1:
            return
        _insert(arr, n - 1)
        key = arr[n - 1]
        j = n - 2
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]; j -= 1
        arr[j + 1] = key

    _insert(lst, len(lst))
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        print(recursive_insertion_sort(t))
