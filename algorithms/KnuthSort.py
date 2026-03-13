# Knuth Sort (3-way QuickSort / Dutch Flag) - O(n log n) avg, O(n) for duplicates
# Autorstwa Donalda Knutha - 3-way partition QuickSort.
# Dzieli na 3 grupy: < pivot, == pivot, > pivot.
# Dramatically faster than regular QuickSort when there are many duplicates.
# Unstable | In-place | "The Art of Computer Programming" vol. 3

from data import *

def knuth_sort(lista):
    lst = lista.copy()

    def sort3(arr, lo, hi):
        if hi <= lo:
            return
        lt, gt = lo, hi
        pivot = arr[lo]
        i = lo + 1
        while i <= gt:
            if arr[i] < pivot:
                arr[lt], arr[i] = arr[i], arr[lt]
                lt += 1; i += 1
            elif arr[i] > pivot:
                arr[i], arr[gt] = arr[gt], arr[i]
                gt -= 1
            else:
                i += 1
        sort3(arr, lo, lt - 1)
        sort3(arr, gt + 1, hi)

    sort3(lst, 0, len(lst) - 1)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(knuth_sort(t))
