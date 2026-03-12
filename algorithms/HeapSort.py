# Heap Sort - O(n log n)
# Buduje max-heap z listy (rodzic zawsze większy od dzieci),
# potem wielokrotnie wyciąga największy element na koniec.
# Niestabilny | In-place | Gwarantowane O(n log n) zawsze

from data import *

def heapify(lst, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and lst[l] > lst[largest]:
        largest = l
    if r < n and lst[r] > lst[largest]:
        largest = r
    if largest != i:
        lst[i], lst[largest] = lst[largest], lst[i]
        heapify(lst, n, largest)

def heap_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(n // 2 - 1, -1, -1):
        heapify(lst, n, i)
    for i in range(n - 1, 0, -1):
        lst[0], lst[i] = lst[i], lst[0]
        heapify(lst, i, 0)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(heap_sort(t))
