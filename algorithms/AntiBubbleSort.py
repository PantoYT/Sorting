# Anti-Bubble Sort - O(n²)
# The exact opposite of Bubble Sort: scans for pairs in CORRECT order
# and swaps them to WRONG order. Efficiently unsorts a sorted list.
# Useful for: generating worst-case inputs, testing stability, chaos.
# "Sorts" in descending order if you start from sorted | Satirical

from data import *

def anti_bubble_sort(lista):
    lst = lista.copy()
    n = len(lst)
    # First sort ascending (to have something to anti-sort)
    lst.sort()
    # Now anti-bubble: swap pairs that ARE in correct order
    changed = True
    while changed:
        changed = False
        for i in range(n - 1):
            if lst[i] <= lst[i + 1]:  # correct order -> swap it!
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
                changed = True
    # Result: sorted in DESCENDING order
    # To get ascending, reverse:
    return lst[::-1]

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        r = anti_bubble_sort(t)
        print(f"Correct: {r == sorted(t)}, Result: {r}")
