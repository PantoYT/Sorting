# Unstable Sort - O(n log n)
# HeapSort zmodyfikowany tak żeby CELOWO łamał stabilność -
# elementy równe są umieszczane w odwróconej kolejności względem oryginału.
# Używany do testowania czy kod nie polega na stabilności sortu.
# Celowo Niestabilny | In-place | Narzędzie testowe / edukacyjne

from data import *

def unstable_sort(lista):
    lst = lista.copy()
    n = len(lst)

    # heapify z odwróconym tie-breaking (celowo niestabilny)
    def heapify(arr, n, i):
        largest = i
        l, r = 2 * i + 1, 2 * i + 2
        # celowy niestabilny: preferuj prawego dziecka przy równości
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
