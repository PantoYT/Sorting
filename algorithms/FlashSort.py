# Flash Sort - O(n) avg
# Classifies elements into classes based on their values (similar to BucketSort),
# then performs cyclic permutation to place them, followed by InsertionSort.
# Unstable | In-place | Very fast with uniform distribution

from data import *

def flash_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    m = max(1, int(0.45 * n))
    min_val, max_val = min(lst), max(lst)
    if min_val == max_val:
        return lst
    L = [0] * m
    for x in lst:
        k = int((m - 1) * (x - min_val) / (max_val - min_val))
        L[k] += 1
    for i in range(1, m):
        L[i] += L[i - 1]
    hold = lst[0]
    j = 0
    k = m - 1
    nmove = 0
    while nmove < n:
        while j > L[k] - 1:
            j += 1
            k = int((m - 1) * (lst[j] - min_val) / (max_val - min_val))
        flash = lst[j]
        while j != L[k]:
            k = int((m - 1) * (flash - min_val) / (max_val - min_val))
            hold = lst[L[k] - 1]
            lst[L[k] - 1] = flash
            L[k] -= 1
            flash = hold
            nmove += 1
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(flash_sort(t))
