# Naive Sort - O(n²) to O(n³) depending on implementation
# "Naive" sort — checks if the list is sorted, if not
# swaps the FIRST bad pair found and restarts from scratch.
# Conceptually the simplest possible sort (besides BogoSort).
# Unstable | In-place | Great teaching example of what NOT to do

from data import *

def naive_sort(lista):
    lst = lista.copy()
    n = len(lst)
    i = 0
    while i < n - 1:
        if lst[i] > lst[i + 1]:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
            i = 0  # restart from scratch after each swap
        else:
            i += 1
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(naive_sort(t))
