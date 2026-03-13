# Shuffle Sort - O(n log n) expected
# Randomly shuffles the array, checks if sorted. If not, shuffles again.
# Identical to BogoSort conceptually but uses Fisher-Yates shuffle
# (guaranteed uniform random permutation each attempt).
# Not for production | Satirical | Expected O(n * n!) time

from data import *
import random

def shuffle_sort(lista):
    lst = lista.copy()
    attempts = 0
    max_attempts = 100000
    while lst != sorted(lst):
        # Fisher-Yates shuffle
        for i in range(len(lst) - 1, 0, -1):
            j = random.randint(0, i)
            lst[i], lst[j] = lst[j], lst[i]
        attempts += 1
        if attempts >= max_attempts:
            break
    return lst

if __name__ == "__main__":
    # only small lists!
    print(shuffle_sort([3, 1, 2, 5, 4]))
    print(shuffle_sort(losowa))
