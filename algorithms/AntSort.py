# Ant Colony Sort (ACO Sort) - O(iterations * n²)
# Inspired by ant colony optimization: virtual ants traverse the array,
# deposit pheromones on correctly-ordered pairs.
# Pairs with more pheromone are more likely to stay, others get swapped.
# Probabilistic | O(n) memory | Converges to sorted state

from data import *
import random

ANTS = 10
ITERATIONS = 50
EVAPORATION = 0.1
PHEROMONE_DEPOSIT = 1.0

def ant_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    # pheromone[i] = strength of "keep pair (i, i+1) in this order"
    pheromone = [1.0] * (n - 1)

    for iteration in range(ITERATIONS):
        # each ant walks the array and votes on swaps
        for ant in range(ANTS):
            for i in range(n - 1):
                if lst[i] > lst[i + 1]:
                    # wrong order: low pheromone -> swap
                    if random.random() > pheromone[i] / (pheromone[i] + 1):
                        lst[i], lst[i + 1] = lst[i + 1], lst[i]
                        pheromone[i] = max(0.1, pheromone[i] - EVAPORATION)
                    else:
                        pheromone[i] += PHEROMONE_DEPOSIT
                else:
                    # correct order: reinforce
                    pheromone[i] = min(10.0, pheromone[i] + PHEROMONE_DEPOSIT * 0.5)

        # pheromone evaporation
        pheromone = [max(0.1, p * (1 - EVAPORATION * 0.1)) for p in pheromone]

    # final cleanup pass
    for _ in range(n):
        for i in range(n - 1):
            if lst[i] > lst[i + 1]:
                lst[i], lst[i + 1] = lst[i + 1], lst[i]
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        r = ant_sort(t)
        print(f"Correct: {r == sorted(t)}, Result: {r}")
