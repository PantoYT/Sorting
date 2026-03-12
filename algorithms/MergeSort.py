# Merge Sort - O(n log n)
# Rekurencyjnie dzieli listę na połowy aż zostają jednoelementowe kawałki,
# potem scala je w posortowane pary, czwórki, ósemki itd.
# Stabilny | O(n) pamięci | Dobry dla dużych danych i linked list

from data import *

def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result.extend(left[i:])
    result.extend(right[j:])
    return result

def merge_sort(lista):
    lst = lista.copy()
    if len(lst) <= 1:
        return lst
    mid = len(lst) // 2
    left = merge_sort(lst[:mid])
    right = merge_sort(lst[mid:])
    return merge(left, right)

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(merge_sort(t))
