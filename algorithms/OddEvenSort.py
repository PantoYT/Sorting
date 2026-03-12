# Odd-Even Sort - O(n²)
# Jak Bubble Sort ale z dwoma naprzemiennymi fazami:
# faza parzysta: porównuje pary (0,1), (2,3), (4,5)...
# faza nieparzysta: porównuje pary (1,2), (3,4), (5,6)...
# Stabilny | In-place | Zaprojektowany do przetwarzania równoległego

from data import *

def odd_even_sort(lista):
    lst = lista.copy()
    n = len(lst)
    sorted_ = False
    while not sorted_:
        sorted_ = True
        for i in range(0, n - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted_ = False
        for i in range(1, n - 1, 2):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                sorted_ = False
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(odd_even_sort(t))
