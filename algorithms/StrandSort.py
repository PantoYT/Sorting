# Strand Sort - O(n²) worst, O(n) best
# Wielokrotnie wyciąga rosnące podciągi ("strand") z listy i scala je.
# Naturalnie wydajny na częściowo posortowanych danych.
# Stabilny | O(n) pamięci

from data import *

def merge(a, b):
    result = []
    i = j = 0
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            result.append(a[i]); i += 1
        else:
            result.append(b[j]); j += 1
    result.extend(a[i:])
    result.extend(b[j:])
    return result

def strand_sort(lista):
    lst = lista.copy()
    result = []
    while lst:
        strand = [lst.pop(0)]
        remaining = []
        for x in lst:
            if x >= strand[-1]:
                strand.append(x)
            else:
                remaining.append(x)
        lst = remaining
        result = merge(result, strand)
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(strand_sort(t))
