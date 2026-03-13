# Drunk Sort - O(?) — the "drunk" algorithm
# 70% chance of a good move (swap if wrong order),
# 30% chance of a completely random swap.
# Eventually gets there... usually.

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
