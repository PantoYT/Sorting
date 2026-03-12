# Cocktail Shaker Sort - O(n²)
# Bubble Sort w obu kierunkach naprzemiennie -
# raz od lewej do prawej, raz od prawej do lewej.
# Szybciej radzi sobie z "żółwiami" (małe elementy na końcu).
# Stabilny | In-place

from data import *

def cocktail_sort(lista):
    lst = lista.copy()
    n = len(lst)
    start, end = 0, n - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start, end):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        end -= 1
        for i in range(end, start, -1):
            if lst[i] < lst[i - 1]:
                lst[i], lst[i - 1] = lst[i - 1], lst[i]
                swapped = True
        start += 1
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(cocktail_sort(t))
