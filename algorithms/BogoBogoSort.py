# BogoBogoSort - O((n+1)!) - WARNING: do not use on lists with > 4 elements!
# For each prefix applies BogoSort. If the prefix stops being
# sorted after adding the next element, starts over.
# Complexity is practically infinite for n > 4.

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
