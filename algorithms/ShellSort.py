# Shell Sort - O(n log²n)
# Ulepszona wersja Insertion Sort - najpierw sortuje elementy oddalone o duży
# odstęp (gap), stopniowo zmniejsza gap aż do 1.
# Niestabilny | In-place | Znacznie szybszy od InsertionSort na dużych danych

from data import *

def shell_sort(lista):
    lst = lista.copy()
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(shell_sort(t))
