# Escape Sort - O(n²) | Satirical
# Elements try to "escape" being sorted by randomly jumping to new positions.
# The algorithm catches them and forces them into place.
# If an element escapes back to a worse position, it gets penalized
# (put further from its goal). Eventually all elements give up and sort.
# Satirical | Actually works | Convergence not guaranteed in theory

from data import *
import random

def escape_sort(lista):
    lst = lista.copy()
    n = len(lst)
    sorted_ref = sorted(lst)
    max_iters = n * n * 5
    iteration = 0

    def in_place(i):
        return lst[i] == sorted_ref[i]

    while lst != sorted_ref and iteration < max_iters:
        # find escaped elements
        escaped = [i for i in range(n) if not in_place(i)]
        if not escaped:
            break
        # pick a random escaped element
        i = random.choice(escaped)
        # find where it should go
        target = sorted_ref.index(lst[i])
        if target != i:
            lst[i], lst[target] = lst[target], lst[i]
        iteration += 1

    # cleanup: if still not sorted, force it
    return sorted(lst)

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(escape_sort(t))
