# Postman Sort - O(nk)
# Historical algorithm used for sorting mail.
# MSD Radix Sort — sorts from most significant digit
# (like mail: first country, then region, then city).
# Stable | O(n + k) memory

from data import *

def postman_sort(lista):
    lst = lista.copy()
    max_val = max(lst)
    num_digits = len(str(max_val))

    def sort_msd(arr, digit):
        if len(arr) <= 1 or digit < 0:
            return arr
        divisor = 10 ** digit
        skrzynki = [[] for _ in range(10)]
        for x in arr:
            skrzynki[(x // divisor) % 10].append(x)
        result = []
        for skrzynka in skrzynki:
            if skrzynka:
                result.extend(sort_msd(skrzynka, digit - 1))
        return result

    return sort_msd(lst, num_digits - 1)

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(postman_sort(t))
