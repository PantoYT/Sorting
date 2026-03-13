# McCarthy Sort - O(n! * n) worst case, often better
# Recursive algorithm: if array is sorted, return it.
# Otherwise remove a random element and recursively sort the rest.
# Named after John McCarthy (inventor of LISP and recursion advocate).
# WARNING: Shrinks the list by removing elements! Not a stable sort.
# Satirical | Destructive (loses elements) | Do not use on data you care about

from data import *
import random

def mccarthy_sort(lista):
    lst = lista.copy()

    def _sort(arr):
        n = len(arr)
        # check if sorted
        for i in range(n - 1):
            if arr[i] > arr[i + 1]:
                # not sorted - remove a random element and recurse
                new_arr = arr[:]
                rand_idx = random.randint(0, n - 1)
                new_arr.pop(rand_idx)
                return _sort(new_arr)
        return arr

    return _sort(lst)

if __name__ == "__main__":
    # WARNING: output may have fewer elements than input!
    for t in [losowa, prawie_posort, duplikaty]:
        result = mccarthy_sort(t)
        print(f"In: {len(t)} elements -> Out: {len(result)} elements: {result}")
