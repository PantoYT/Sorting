# Sample Sort - O(n log n) average
# Parallel-friendly generalization of QuickSort to p processors.
# Picks s*p sample elements, sorts them to find p-1 splitters,
# partitions data into p buckets, sorts each bucket.
# Stable | O(n) memory | Great for distributed/parallel sorting

from data import *

def sample_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 16:
        return sorted(lst)

    # pick sqrt(n) samples, sort them, use as splitters
    import random
    num_buckets = max(2, int(n ** 0.5))
    sample_size = min(n, num_buckets * 3)
    samples = sorted(random.sample(lst, sample_size))

    # pick evenly spaced splitters
    splitters = [samples[i * len(samples) // num_buckets]
                 for i in range(1, num_buckets)]

    # partition into buckets
    buckets = [[] for _ in range(num_buckets)]
    for x in lst:
        placed = False
        for i, s in enumerate(splitters):
            if x <= s:
                buckets[i].append(x)
                placed = True
                break
        if not placed:
            buckets[-1].append(x)

    # sort each bucket and concatenate
    result = []
    for bucket in buckets:
        result.extend(sorted(bucket))
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(sample_sort(t))
