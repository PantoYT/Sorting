# Gnome Sort - O(n²)
# Like a garden gnome — moves right, if element is out of place
# steps back and swaps, then moves right again.
# Stable | In-place | Prosta implementacja ale wolny

from data import *

def gnome_sort(lista):
    lst = lista.copy()
    n = len(lst)
    i = 0
    while i < n:
        if i == 0 or lst[i] >= lst[i - 1]:
            i += 1
        else:
            lst[i], lst[i - 1] = lst[i - 1], lst[i]
            i -= 1
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(gnome_sort(t))
