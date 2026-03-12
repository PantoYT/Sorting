# Pigeonhole Sort - O(n + k)
# Tworzy osobną "skrzynkę" dla każdej możliwej wartości i wrzuca tam elementy.
# Podobny do Counting Sort ale zachowuje same elementy zamiast ich zliczać.
# Stabilny | O(n + k) pamięci | Dobry gdy zakres ≈ liczba elementów

from data import *

def pigeonhole_sort(lista):
    lst = lista.copy()
    min_val, max_val = min(lst), max(lst)
    holes = [[] for _ in range(max_val - min_val + 1)]
    for x in lst:
        holes[x - min_val].append(x)
    result = []
    for hole in holes:
        result.extend(hole)
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(pigeonhole_sort(t))
