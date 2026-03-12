# Gnome Sort - O(n²)
# Jak ogrodnik gnome - idzie w prawo, jeśli element jest nie na miejscu
# cofa się i zamienia, potem idzie znowu w prawo.
# Stabilny | In-place | Prosta implementacja ale wolny

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
