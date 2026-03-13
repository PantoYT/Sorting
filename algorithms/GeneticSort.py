# Genetic Sort - O(generations × population × n)
# Evolutionary algorithm: maintains a population of permutations,
# selects the fittest (most sorted), performs crossover and mutation
# to breed the next generation. Falls back to sorted() if needed.
# Fitness = number of correctly ordered adjacent pairs.
# Probabilistic | O(population × n) memory | Educational

from data import *
import random

POPULATION = 20
GENERATIONS = 150
MUTATION_RATE = 0.03

def _fitness(perm):
    return sum(1 for i in range(len(perm) - 1) if perm[i] <= perm[i + 1])

def _mutate(perm, rate):
    lst = perm[:]
    for i in range(len(lst)):
        if random.random() < rate:
            j = random.randint(0, len(lst) - 1)
            lst[i], lst[j] = lst[j], lst[i]
    return lst

def _crossover(p1, p2):
    """Order crossover (OX1) — preserves relative order."""
    n = len(p1)
    a, b = sorted(random.sample(range(n), 2))
    child = [None] * n
    child[a:b] = p1[a:b]
    fill = [x for x in p2 if x not in child[a:b]]
    k = 0
    for i in range(n):
        if child[i] is None:
            child[i] = fill[k]; k += 1
    return child

def genetic_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    population = [random.sample(lst, n) for _ in range(POPULATION)]
    best = None

    for _ in range(GENERATIONS):
        population.sort(key=_fitness, reverse=True)
        best = population[0]
        if _fitness(best) == n - 1:
            return best  # perfect

        elite = population[:max(2, POPULATION // 4)]
        new_pop = elite[:]
        while len(new_pop) < POPULATION:
            p1, p2 = random.choices(elite, k=2)
            child = _mutate(_crossover(p1, p2), MUTATION_RATE)
            new_pop.append(child)
        population = new_pop

    # fallback: if genetic didn't converge, return sorted
    if best is None or _fitness(best) < n - 1:
        return sorted(lst)
    return best

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        r = genetic_sort(t)
        print(f"Correct: {r == sorted(t)}, Result: {r}")
