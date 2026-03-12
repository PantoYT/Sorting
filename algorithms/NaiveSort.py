# Naive Sort - O(n²) do O(n³) zależnie od implementacji
# "Naiwny" sort - sprawdza czy lista jest posortowana, jeśli nie
# to zamienia PIERWSZĄ znalezioną złą parę i zaczyna sprawdzanie od nowa.
# Konceptualnie najprostszy możliwy sort (poza BogoSort).
# Niestabilny | In-place | Świetny jako przykład dydaktyczny czego NIE robić

from data import *

def naive_sort(lista):
    lst = lista.copy()
    n = len(lst)
    i = 0
    while i < n - 1:
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = 0  # zacznij od nowa po każdej zamianie
        else:
            i += 1
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(naive_sort(t))
