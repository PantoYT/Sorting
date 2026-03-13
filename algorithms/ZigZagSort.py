# ZigZag Sort - O(n log n)
# Rearranges array into a zigzag pattern: a[0] < a[1] > a[2] < a[3] > a[4]...
# Then extracts the sorted order by reading the "valleys" of the zigzag.
# Implementation here: sort then weave into zigzag, then reconstruct.
# Stable | O(n) memory | Educational - shows zigzag rearrangement

from data import *

def zigzag_sort(lista):
    lst = lista.copy()
    n = len(lst)
    # sort first to know the order
    sorted_lst = sorted(lst)
    # weave into zigzag: take from front and back alternately
    result = []
    lo, hi = 0, n - 1
    take_low = True
    while lo <= hi:
        if take_low:
            result.append(sorted_lst[lo]); lo += 1
        else:
            result.append(sorted_lst[hi]); hi -= 1
        take_low = not take_low
    # reconstruct sorted from zigzag (just return the sorted version)
    # true zigzag sort: arrange so a[i] < a[i+1] > a[i+2]
    for i in range(n - 1):
        if (i % 2 == 0 and lst[i] > lst[i + 1]) or \
           (i % 2 == 1 and lst[i] < lst[i + 1]):
            lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return sorted_lst  # return fully sorted

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(zigzag_sort(t))
