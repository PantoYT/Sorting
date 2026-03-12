# Drunk Sort - O(?) - algorytm który jest "pijany"
# 70% szans na dobry ruch (zamiana jeśli zła kolejność),
# 30% szans na całkowicie losową zamianę.
# Ostatecznie dochodzi do celu... zazwyczaj.

from data import *
import random

def drunk_sort(lista):
    lst = lista.copy()
    n = len(lst)
    max_attempts = 10000
    attempts = 0

    def is_sorted(l):
        return all(l[i] <= l[i + 1] for i in range(len(l) - 1))

    while not is_sorted(lst) and attempts < max_attempts:
        i = random.randint(0, n - 2)
        if random.random() < 0.7:
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
        else:
            j = random.randint(0, n - 1)
            lst[i], lst[j] = lst[j], lst[i]
        attempts += 1

    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, duplikaty]
    for t in testy:
        print(drunk_sort(t))
