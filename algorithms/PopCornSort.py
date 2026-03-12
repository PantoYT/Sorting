# Popcorn Sort - O(n²)
# Wariant BubbleSort gdzie elementy "wyskakują" na właściwą pozycję.
# Każdy element przesuwa się zarówno w prawo jak i w lewo dopóki nie trafi na miejsce.
# Stabilny | In-place

from data import *

def popcorn_sort(lista):
    lst = lista.copy()
    n = len(lst)
    sorted_ = False
    while not sorted_:
        sorted_ = True
        i = 0
        while i < n:
            j = i
            while j < n - 1 and lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
                j += 1
                sorted_ = False
            while j > 0 and lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
                j -= 1
                sorted_ = False
            i += 1
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(popcorn_sort(t))
