# Reverse Bubble Sort - O(n²)
# Bubble Sort scanning from RIGHT to LEFT instead of left to right.
# Smaller elements "sink" to the front instead of larger ones "bubbling" to back.
# Functionally identical to BubbleSort but traversal direction reversed.
# Stable | In-place | Educational mirror of BubbleSort

from data import *

def reverse_bubble_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - 1, i, -1):  # scan right to left
            if lst[j] < lst[j - 1]:
                lst[j], lst[j - 1] = lst[j - 1], lst[j]
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(reverse_bubble_sort(t))
