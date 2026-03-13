# Hybrid Sort - O(n log n)
# Adaptively chooses the best algorithm based on input characteristics:
# - Nearly sorted (few inversions)? -> InsertionSort
# - Many duplicates? -> CountingSort
# - Large random? -> TimSort
# - Small? -> InsertionSort
# The benchmark algorithm for real-world adaptive sorting.
# Stable | Adaptive | Best algorithm for unknown input distributions

from data import *

def count_inversions_approx(lst, sample_size=20):
    """Approximate inversion count via sampling."""
    import random
    n = len(lst)
    if n <= sample_size:
        return sum(1 for i in range(n) for j in range(i+1,n) if lst[i]>lst[j])
    indices = sorted(random.sample(range(n), sample_size))
    sample = [lst[i] for i in indices]
    return sum(1 for i in range(len(sample)) for j in range(i+1,len(sample))
               if sample[i] > sample[j])

def hybrid_sort(lista):
    lst = lista.copy()
    n = len(lst)

    if n <= 16:
        # small: insertion sort
        for i in range(1, n):
            key = lst[i]; j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j+1] = lst[j]; j -= 1
            lst[j+1] = key
        return lst

    unique_ratio = len(set(lst)) / n
    inversions = count_inversions_approx(lst)

    if inversions <= 5:
        # nearly sorted: insertion sort
        for i in range(1, n):
            key = lst[i]; j = i - 1
            while j >= 0 and lst[j] > key:
                lst[j+1] = lst[j]; j -= 1
            lst[j+1] = key
        return lst
    elif unique_ratio < 0.3 and all(isinstance(x, int) for x in lst):
        # many duplicates + integers: counting sort
        mn, mx = min(lst), max(lst)
        count = [0] * (mx - mn + 1)
        for x in lst: count[x-mn] += 1
        result = []
        for i, c in enumerate(count): result.extend([i+mn]*c)
        return result
    else:
        # general: timsort (Python's built-in)
        return sorted(lst)

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(hybrid_sort(t))
