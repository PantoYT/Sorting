# Radix Sort - O(nk), k = liczba cyfr
# Sortuje po kolejnych cyfrach od najmniej znaczącej (LSD) do najbardziej.
# Używa Counting Sort jako pomocniczego dla każdej cyfry.
# Stabilny | O(n + k) pamięci | Świetny dla liczb całkowitych

from data import *

def counting_sort_by_digit(lst, exp):
    n = len(lst)
    output = [0] * n
    count = [0] * 10
    for x in lst:
        count[(x // exp) % 10] += 1
    for i in range(1, 10):
        count[i] += count[i - 1]
    for i in range(n - 1, -1, -1):
        idx = (lst[i] // exp) % 10
        output[count[idx] - 1] = lst[i]
        count[idx] -= 1
    return output

def radix_sort(lista):
    lst = lista.copy()
    exp = 1
    while max(lst) // exp > 0:
        lst = counting_sort_by_digit(lst, exp)
        exp *= 10
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(radix_sort(t))
