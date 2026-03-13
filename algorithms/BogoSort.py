# Bogo Sort - O(n * n!) avg, may never finish
# Randomly shuffles the list until sorted.
# Theoretically may never finish (infinite worst-case complexity).
# Unstable | In-place | Absolutely useless, legendary

from data import *
import random

def bogo_sort(lista):
    lst = lista.copy()
    while lst != sorted(lst):
        random.shuffle(lst)
    return lst

if __name__ == "__main__":
    # small list only!
    print(bogo_sort(losowa))
