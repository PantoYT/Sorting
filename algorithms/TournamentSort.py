# Tournament Sort - O(n log n)
# Builds a tournament tree (like in sports) — winner of each round advances.
# Repeatedly extracts the minimum, replaces it with INF and updates the tree.
# Unstable | O(n) memory | Similar to HeapSort

from data import *
import math

def tournament_sort(lista):
    lst = lista.copy()
    n = len(lst)
    size = 2 ** math.ceil(math.log2(n)) if n > 1 else 1
    INF = float('inf')
    padded = lst + [INF] * (size - n)
    tree = [INF] * (2 * size)
    for i in range(size):
        tree[size + i] = padded[i]
    for i in range(size - 1, 0, -1):
        tree[i] = min(tree[2 * i], tree[2 * i + 1])
    result = []
    for _ in range(n):
        result.append(tree[1])
        i = 1
        while i < size:
            i = 2 * i if tree[2 * i] == tree[i] else 2 * i + 1
        tree[i] = INF
        i //= 2
        while i >= 1:
            tree[i] = min(tree[2 * i], tree[2 * i + 1])
            i //= 2
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(tournament_sort(t))
