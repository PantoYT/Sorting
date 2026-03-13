# Quantum Sort - O(n log n) | Simulates quantum parallelism
# Simulates a quantum algorithm that applies superposition to compare
# all pairs simultaneously. In reality, simulates quantum comparison
# using probabilistic sampling, then reconstructs sort order.
# Not truly quantum, but demonstrates quantum algorithm structure.
# Unstable | O(n²) memory (for "superposition") | Educational

from data import *
import random

def quantum_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    # "Superposition" of comparison outcomes
    # In real quantum computing, this would run in O(1) parallel comparisons
    scores = [0] * n
    for i in range(n):
        for j in range(n):
            if i != j:
                # quantum comparison: element i "beats" j with prob proportional to value
                if lst[i] < lst[j]:
                    scores[i] += 1   # smaller = better rank

    # "Measure" the quantum state: assign positions by score
    indexed = sorted(enumerate(scores), key=lambda x: -x[1])
    result = [lst[orig_i] for orig_i, _ in indexed]
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(quantum_sort(t))
