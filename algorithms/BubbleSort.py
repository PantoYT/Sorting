# Bubble Sort - O(n²)
# Porównuje sąsiednie elementy i zamienia je jeśli są w złej kolejności.
# Większe wartości "wypływają" na koniec listy jak bąbelki.
# Stabilny | In-place

from data import *

def bubble_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(bubble_sort(t))
