# Quantum Bogo Sort - O(1) - probably
#
# Complexity:  O(1) — one quantum observation
# Memory:      O(n!) superposition states
# Stability:   depends on which universe you're in
#
# How it works:
# 1. The list exists in superposition of all n! possible orderings simultaneously.
# 2. Observe the multiverse. Somewhere out there, it's already sorted.
# 3. Tune your quantum antenna to that universe.
# 4. Read off the result. Done.
#
# No universes are harmed in the process.
# We're just borrowing a sorted state from a parallel branch.
# They probably have a spare.
#
# Source: https://en.wikipedia.org/wiki/Bogosort#Quantum_bogosort

from data import *
import random
import time
import itertools


class MultiverseObserver:
    """Scans parallel universes for one where the list is already sorted."""

    def __init__(self, lst):
        self.lst = lst
        all_perms = list(itertools.permutations(lst))
        amp = 1.0 / (len(all_perms) ** 0.5)
        self.superposition = {perm: amp for perm in all_perms}
        print(f"  [QUANTUM]: Superposition initialised — {len(all_perms)} universes in range")
        print(f"  [QUANTUM]: Scanning for a sorted one...")

    def find_sorted_universe(self):
        """Locate the branch of the multiverse where the list is sorted.
        Does not destroy anything. Just looks."""
        candidates = {
            perm: amp
            for perm, amp in self.superposition.items()
            if all(perm[i] <= perm[i + 1] for i in range(len(perm) - 1))
        }
        borrowed = len(self.superposition) - len(candidates)
        print(f"  [QUANTUM]: Checked {len(self.superposition)} universes")
        print(f"  [QUANTUM]: {borrowed} skipped (unsorted, left undisturbed)")
        print(f"  [QUANTUM]: {len(candidates)} sorted universe(s) located ✓")
        self.superposition = candidates

    def observe(self):
        """Collapse the wave function by observing the sorted universe."""
        if not self.superposition:
            raise ValueError("No sorted universe found — quantum paradox. Try a different list.")
        states  = list(self.superposition.keys())
        weights = [abs(a) ** 2 for a in self.superposition.values()]
        total   = sum(weights)
        weights = [w / total for w in weights]
        chosen  = random.choices(states, weights=weights)[0]
        print(f"  [QUANTUM]: Wave function collapsed. Result borrowed from parallel branch.")
        return list(chosen)


def quantum_bogo_sort(lista):
    lst = lista.copy()
    n   = len(lst)

    print(f"\n{'─'*54}")
    print(f"  QUANTUM BOGO SORT  (n={n})")
    print(f"{'─'*54}")

    import math
    factorial = math.factorial(n)

    if factorial > 10 ** 6:
        # Too many universes to enumerate — fall back to random sampling.
        # Conceptually identical: keep drawing from the multiverse until
        # we land on a sorted branch. No universes harmed either way.
        print(f"  n={n}  →  {factorial:,} possible orderings")
        print(f"  Multiverse is large. Sampling instead of full scan...")
        attempts = 0
        while lst != sorted(lst):
            random.shuffle(lst)
            attempts += 1
            if attempts % 500 == 0:
                print(f"  [QUANTUM]: Still scanning... ({attempts} branches checked so far)")
        print(f"  [QUANTUM]: Found one after {attempts} samples.")
        print(f"{'─'*54}\n")
        return lst

    # Small list: full superposition scan
    t0      = time.perf_counter()
    obs     = MultiverseObserver(lst)
    time.sleep(0.03)
    obs.find_sorted_universe()
    time.sleep(0.01)
    result  = obs.observe()
    elapsed = (time.perf_counter() - t0) * 1000

    print(f"  [QUANTUM]: Done in {elapsed:.2f}ms (classical simulation)")
    print(f"{'─'*54}\n")
    return result


if __name__ == "__main__":
    sample = [3, 1, 4, 2, 5]
    print(f"Input:  {sample}")
    result = quantum_bogo_sort(sample)
    print(f"Output: {result}")
    print(f"Correct: {result == sorted(sample)}")
    print()
    print("Complexity:")
    print("  Time:  O(1) — just an observation")
    print("  Space: O(n!) superpositions")
    print()
    print("Theorem: the sorted version of your list already exists")
    print("somewhere in the multiverse. We just needed to look.")
