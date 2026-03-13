# Gravity Sort - O(n * max)
# Inna implementacja tej samej idei co BeadSort.
# Boolean grid — True = bead, False = empty slot.
# Beads "fall" down through columns.
# Stable | Only works on non-negative integers

from data import *

def gravity_sort(lista):
    lst = lista.copy()
    if any(x < 0 for x in lst):
        raise ValueError("Gravity sort only works on non-negative integers")
    n = len(lst)
    max_val = max(lst)
    grid = [[j < lst[i] for j in range(max_val)] for i in range(n)]
    for col in range(max_val):
        count = sum(grid[row][col] for row in range(n))
        for row in range(n):
            grid[row][col] = row >= n - count
    return [sum(row) for row in grid]

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(gravity_sort(t))
