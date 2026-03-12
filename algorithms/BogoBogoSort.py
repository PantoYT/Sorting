# BogoBogoSort - O((n+1)!) - UWAGA: nie używać na listach > 4 elementów!
# Dla każdego prefiksu listy stosuje BogoSort. Jeśli prefiks przestaje być
# posortowany po dodaniu następnego elementu, zaczyna od nowa.
# Złożoność jest praktycznie nieskończona dla n > 4.

from data import *
import random

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def bogobogo_sort(lista):
    lst = lista.copy()
    n = len(lst)
    i = 1
    while i <= n:
        prefix = lst[:i]
        random.shuffle(prefix)
        lst[:i] = prefix
        if is_sorted(lst[:i]):
            i += 1
        else:
            i = 1
    return lst

if __name__ == "__main__":
    print(bogobogo_sort([3, 1, 2]))
    print(bogobogo_sort([4, 2, 1, 3]))
