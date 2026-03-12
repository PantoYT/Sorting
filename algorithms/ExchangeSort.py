# Exchange Sort - O(n²)
# Każdy element porównuje się ze WSZYSTKIMI następnymi (nie tylko sąsiednim).
# Jak Selection Sort ale zamienia od razu zamiast szukać minimum.
# Niestabilny | In-place | Wygląda jak BubbleSort ale nie jest - inna kolejność zamian

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
