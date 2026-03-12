# Insertion Sort - O(n²), O(n) dla prawie posortowanych
# Bierze kolejny element i "wsuwa" go na właściwe miejsce w posortowanej części.
# Jak sortowanie kart w ręce - każda nowa karta trafia na swoje miejsce.
# Stabilny | In-place | Bardzo szybki na małych i prawie posortowanych danych

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
