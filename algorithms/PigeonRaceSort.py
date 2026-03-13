# Pigeon Race Sort - O(n + k) | Satirical
# Homing pigeons carry "messages" (values) to their destination holes.
# Each pigeon is released simultaneously (parallel by nature).
# Faster pigeons (smaller values) arrive at lower-numbered holes first.
# In practice: exactly counting sort, but with pigeons.
# Stable | O(n + k) memory | Satirical variant of PigeonholeSort

from data import *
import time

def pigeon_race_sort(lista):
    lst = lista.copy()
    mn, mx = min(lst), max(lst)
    print(f"[PigeonRace]: Releasing {len(lst)} pigeons to {mx - mn + 1} holes...")
    coops = [[] for _ in range(mx - mn + 1)]
    for pigeon in lst:
        coops[pigeon - mn].append(pigeon)
    print(f"[PigeonRace]: All pigeons landed. Collecting results...")
    result = []
    for coop in coops:
        result.extend(coop)
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        print(pigeon_race_sort(t))
