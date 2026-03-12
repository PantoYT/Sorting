# Selection Sort - O(n²)
# Znajduje najmniejszy element w nieposortowanej części i wstawia go na początek.
# Przesuwa granicę posortowanej części o 1 w każdej iteracji.
# Niestabilny | In-place

from data import *

def selection_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if lst[j] < lst[min_idx]:
                min_idx = j
        lst[i], lst[min_idx] = lst[min_idx], lst[i]
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(selection_sort(t))
