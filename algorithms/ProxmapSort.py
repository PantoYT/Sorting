# Proxmap Sort - O(n) average
# Maps each element to its approximate position using a linear function,
# then uses insertion sort within each "proxmap" bucket.
# Similar to Bucket Sort but uses a smarter mapping function.
# Unstable | O(n) memory | Very fast on uniformly distributed data

from data import *

def proxmap_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    mn, mx = min(lst), max(lst)
    if mn == mx:
        return lst
    # map each value to a bucket index in [0, n-1]
    def map_key(x):
        return int((x - mn) / (mx - mn + 1) * n)

    buckets = [[] for _ in range(n)]
    for x in lst:
        buckets[map_key(x)].append(x)

    result = []
    for bucket in buckets:
        # insertion sort within bucket
        for i in range(1, len(bucket)):
            key = bucket[i]
            j = i - 1
            while j >= 0 and bucket[j] > key:
                bucket[j + 1] = bucket[j]; j -= 1
            bucket[j + 1] = key
        result.extend(bucket)
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(proxmap_sort(t))
