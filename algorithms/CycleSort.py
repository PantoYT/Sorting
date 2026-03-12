# Cycle Sort - O(n²)
# Minimalizuje liczbę zapisów do pamięci - dla każdego elementu
# liczy ile jest od niego mniejszych (to jego docelowa pozycja)
# i wstawia go tam wprost przez permutację cykliczną.
# Niestabilny | In-place | Optymalny pod względem liczby zapisów

from data import *

def cycle_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for cycle_start in range(n - 1):
        item = lst[cycle_start]
        pos = cycle_start
        for i in range(cycle_start + 1, n):
            if lst[i] < item:
                pos += 1
        if pos == cycle_start:
            continue
        while item == lst[pos]:
            pos += 1
        lst[pos], item = item, lst[pos]
        while pos != cycle_start:
            pos = cycle_start
            for i in range(cycle_start + 1, n):
                if lst[i] < item:
                    pos += 1
            while item == lst[pos]:
                pos += 1
            lst[pos], item = item, lst[pos]
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(cycle_sort(t))
