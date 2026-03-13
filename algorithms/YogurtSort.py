# Yogurt Sort - O(n²)
# Named after the fermentation process: elements "culture" into sorted groups.
# Scans forward collecting elements that belong to a sorted "culture",
# then merges cultures left to right like merging fermentation batches.
# Stable | O(n) memory | Original algorithm

from data import *

def yogurt_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    # split into "cultures" (maximal non-decreasing runs)
    cultures = []
    start = 0
    for i in range(1, n):
        if lst[i] < lst[i - 1]:
            cultures.append(lst[start:i])
            start = i
    cultures.append(lst[start:])
    # merge all cultures together (like merging fermentation batches)
    result = cultures[0]
    for culture in cultures[1:]:
        merged = []
        i = j = 0
        while i < len(result) and j < len(culture):
            if result[i] <= culture[j]:
                merged.append(result[i]); i += 1
            else:
                merged.append(culture[j]); j += 1
        merged.extend(result[i:])
        merged.extend(culture[j:])
        result = merged
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(yogurt_sort(t))
