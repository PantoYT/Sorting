# Bead Sort - O(S) where S = sum of all elements
# Physical simulation — each number is a row of beads on rods.
# Beads "fall" down columns due to gravity.
# Only works on non-negative integers.

from data import *

def bead_sort(lista):
    lst = lista.copy()
    if any(x < 0 for x in lst):
        raise ValueError("Bead sort only works on non-negative integers")
    n = len(lst)
    max_val = max(lst)
    # grid: grid[i][j] = 1 if element i has a bead on rod j
    grid = [[1 if j < lst[i] else 0 for j in range(max_val)] for i in range(n)]
    # beads fall due to gravity — count how many are in each column
    for col in range(max_val):
        count = sum(grid[row][col] for row in range(n))
        # fill from the bottom
        for row in range(n):
            grid[row][col] = 1 if row >= n - count else 0
    # przelicz wiersze z powrotem na liczby
    return [sum(grid[i]) for i in range(n)]

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(bead_sort(t))
