# Bead Sort - O(S) gdzie S = suma wszystkich elementów
# Symulacja fizyczna - każda liczba to wiersz koralików na drutach.
# Koraliki "opadają" kolumnami zgodnie z grawitacją.
# Działa tylko na liczbach nieujemnych całkowitych.

from data import *

def bead_sort(lista):
    lst = lista.copy()
    if any(x < 0 for x in lst):
        raise ValueError("Bead sort działa tylko na liczbach nieujemnych")
    n = len(lst)
    max_val = max(lst)
    # siatka: grid[i][j] = 1 jeśli element i ma koralik na drucie j
    grid = [[1 if j < lst[i] else 0 for j in range(max_val)] for i in range(n)]
    # koraliki opadają grawitacyjnie - liczymy ile jest w każdej kolumnie
    for col in range(max_val):
        count = sum(grid[row][col] for row in range(n))
        # wypełnij od dołu
        for row in range(n):
            grid[row][col] = 1 if row >= n - count else 0
    # przelicz wiersze z powrotem na liczby
    return [sum(grid[i]) for i in range(n)]

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(bead_sort(t))
