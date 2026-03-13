# Vino Sort (Wine Sort) 🍷 - O(n²)
# Original algorithm inspired by the wine decanting process:
# "good" elements (in their correct place) stay,
# "bad" ones are collected into a "carafe" (separate list), decanted (sorted),
# then poured back into the correct positions.
# Stable | O(n) memory | Original algorithm

from data import *

def vino_sort(lista):
    lst = lista.copy()
    n = len(lst)
    sorted_ref = sorted(lst)

    # collect "bad" elements into the carafe
    karafka = []
    wolne_miejsca = []
    for i in range(n):
        if lst[i] != sorted_ref[i]:
            karafka.append(lst[i])
            wolne_miejsca.append(i)

    # decant the carafe (sort the bad elements)
    karafka.sort()

    # pour back into correct positions
    for i, pos in enumerate(wolne_miejsca):
        lst[pos] = karafka[i]

    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(vino_sort(t) == sorted(t), vino_sort(t))
