# Unstable Sort - O(n log n)
# HeapSort modified to DELIBERATELY break stability —
# equal elements are placed in reverse order relative to the original.
# Used to test whether code incorrectly relies on sort stability.
# Deliberately Unstable | In-place | Testing / educational tool

from data import *

def unstable_sort(lista):
    lst = lista.copy()
    n = len(lst)

    # heapify with reversed tie-breaking (deliberately unstable)
    def heapify(arr, n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        # deliberately unstable: prefer right child on equal values
        if l < n and arr[l] >= arr[largest]:
            largest = l
        if r < n and arr[r] >= arr[largest]:
            largest = r
        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]
            heapify(arr, n, largest)

    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(unstable_sort(t))
