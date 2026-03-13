# Shell Sort - O(n log²n)
# Improved Insertion Sort — first sorts elements separated by a large
# gap, gradually shrinks the gap down to 1.
# Unstable | In-place | Much faster than InsertionSort on large data

from data import *

def shell_sort(lista):
    lst = lista.copy()
    n = len(lst)
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = lst[i]
            j = i
            while j >= gap and lst[j - gap] > temp:
                lst[j] = lst[j - gap]
                j -= gap
            lst[j] = temp
        gap //= 2
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(shell_sort(t))
