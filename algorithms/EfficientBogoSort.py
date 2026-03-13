# Efficient Bogo Sort - O(n!) expected | Still terrible
# "Optimized" BogoSort: checks if array is sorted, if not,
# finds the FIRST out-of-order pair and places it correctly (instead of full shuffle).
# This is actually just a very roundabout way to do selection sort.
# Still awful, but now it's EFFICIENTLY awful.
# Unstable | In-place | O(n²) if you think about it hard enough

from data import *
import random

def efficient_bogo_sort(lista):
    lst = lista.copy()
    n = len(lst)

    def is_sorted(arr):
        return all(arr[i] <= arr[i+1] for i in range(len(arr)-1))

    # "efficiently" fix one pair at a time instead of random shuffle
    max_passes = n * n * 10
    passes = 0
    while not is_sorted(lst) and passes < max_passes:
        # find first problem
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                # "efficiently" fix it... by finding where it should go
                correct_pos = i
                for k in range(i + 1, n):
                    if lst[k] < lst[correct_pos]:
                        correct_pos = k
                lst[i], lst[correct_pos] = lst[correct_pos], lst[i]
                break
        passes += 1
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        print(efficient_bogo_sort(t))
