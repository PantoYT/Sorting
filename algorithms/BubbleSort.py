# Bubble Sort - O(n²)
# Compares adjacent elements and swaps them if they are in the wrong order.
# Larger values "bubble up" to the end of the list.
# Stable | In-place

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
