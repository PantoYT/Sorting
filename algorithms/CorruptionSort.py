# Corruption Sort - O(n log n) + corruption overhead
# Sorts the array correctly, then randomly "corrupts" 5-15% of elements
# by swapping them with slightly wrong neighbors.
# Simulates data corruption in storage systems.
# Not correct (by design) | Use for: testing error detection, chaos engineering

from data import *
import random

CORRUPTION_RATE = 0.08  # 8% of elements get corrupted

def corruption_sort(lista):
    lst = lista.copy()
    n = len(lst)

    # sort correctly first
    lst.sort()

    # then introduce corruption
    corruptions = max(1, int(n * CORRUPTION_RATE))
    for _ in range(corruptions):
        i = random.randint(0, n - 2)
        if random.random() < 0.5:
            lst[i], lst[i + 1] = lst[i + 1], lst[i]

    print(f"[CorruptionSort]: Sorted {n} elements. "
          f"Also corrupted ~{corruptions} of them. You're welcome.")
    return lst

if __name__ == "__main__":
    for t in [losowa, duza]:
        r = corruption_sort(t)
        print(f"Correct: {r == sorted(t)}, Result: {r[:10]}...")
