# Insertion Sort - O(n²), O(n) for nearly sorted
# Takes the next element and "inserts" it into the correct position in the sorted part.
# Like sorting cards in hand — each new card goes to its place.
# Stable | In-place | Very fast on small and nearly-sorted data

from data import *

def insertion_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(insertion_sort(t))
