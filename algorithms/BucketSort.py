# Bucket Sort - O(n + k) avg
# Divides elements into n buckets (ranges), sorts each bucket
# separately (InsertionSort), then concatenates buckets.
# Stable | O(n + k) memory | Great with uniform distribution

from data import *

def insertion_sort_bucket(lst):
    for i in range(1, len(lst)):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key
    return lst

def bucket_sort(lista):
    lst = lista.copy()
    n = len(lst)
    min_val, max_val = min(lst), max(lst)
    buckets = [[] for _ in range(n)]
    for x in lst:
        idx = int((x - min_val) / (max_val - min_val + 1) * n)
        buckets[idx].append(x)
    result = []
    for bucket in buckets:
        result.extend(insertion_sort_bucket(bucket))
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(bucket_sort(t))
