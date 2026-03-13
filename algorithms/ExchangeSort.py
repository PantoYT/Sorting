# Exchange Sort - O(n²)
# Each element is compared with ALL subsequent ones (not just the neighbour).
# Like Selection Sort but swaps immediately instead of finding the minimum.
# Unstable | In-place | Looks like BubbleSort but isn't — different swap order

from data import *

def exchange_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if lst[i] > lst[j]:
                lst[i], lst[j] = lst[j], lst[i]
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(exchange_sort(t))
