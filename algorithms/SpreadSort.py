# Spread Sort - O(n) avg
# Hybrydowy algorytm z biblioteki Boost C++.
# Sortuje bitowo od najbardziej znaczącego bajtu (MSD),
# dla małych partycji przełącza na InsertionSort.
# Niestabilny | In-place | Bardzo szybki w praktyce

from data import *

def insertion_sort(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def spread_sort_helper(lst, shift):
    if len(lst) <= 16:
        return insertion_sort(lst)
    buckets = [[] for _ in range(256)]
    for x in lst:
        buckets[(x >> shift) & 0xFF].append(x)
    result = []
    for bucket in buckets:
        if not bucket:
            continue
        if len(bucket) == 1 or shift == 0:
            result.extend(bucket)
        else:
            result.extend(spread_sort_helper(bucket, shift - 8))
    return result

def spread_sort(lista):
    lst = lista.copy()
    if not lst:
        return lst
    max_val = max(lst)
    shift = 0
    while (max_val >> (shift + 8)) > 0:
        shift += 8
    return spread_sort_helper(lst, shift)

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(spread_sort(t))
