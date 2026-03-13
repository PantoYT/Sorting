# Pancake Sort - O(n²)
# Only allowed operation: reverse a prefix of the list (like flipping pancakes).
# Finds the largest element, reverses prefix to bring it to front,
# then reverses to move it to its final position.
# Unstable | In-place

from data import *

def flip(lst, i):
    return lst[:i + 1][::-1] + lst[i + 1:]

def pancake_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for size in range(n, 1, -1):
        max_i = lst.index(max(lst[:size]))
        if max_i != size - 1:
            lst = flip(lst, max_i)
            lst = flip(lst, size - 1)
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(pancake_sort(t))
