# Counting Sort - O(n + k), k = value range
# Counts occurrences of each value, then reconstructs the sorted list.
# Works only on integers. Very fast when k is small.
# Stable | O(n + k) memory | Not a comparison-based algorithm

from data import *

def counting_sort(lista):
    lst = lista.copy()
    min_val = min(lst)
    max_val = max(lst)
    count = [0] * (max_val - min_val + 1)
    for x in lst:
        count[x - min_val] += 1
    result = []
    for i, c in enumerate(count):
        result.extend([i + min_val] * c)
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(counting_sort(t))
