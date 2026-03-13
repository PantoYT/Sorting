# American Flag Sort - O(nk)
# MSD (Most Significant Digit) Radix Sort — sorts from most significant digit.
# Like sorting mail: first country, then region, then city.
# In-place | Unstable | Good for data with a small digit range

from data import *

def american_flag_sort(lista):
    lst = lista.copy()
    max_val = max(lst)
    num_digits = len(str(max_val))

    def sort_msd(arr, digit_pos):
        if len(arr) <= 1 or digit_pos < 0:
            return arr
        divisor = 10 ** digit_pos
        buckets = [[] for _ in range(10)]
        for x in arr:
            buckets[(x // divisor) % 10].append(x)
        result = []
        for bucket in buckets:
            result.extend(sort_msd(bucket, digit_pos - 1))
        return result

    return sort_msd(lst, num_digits - 1)

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(american_flag_sort(t))
