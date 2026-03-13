# Miracle Sort - complexity: eternity
# Waits for cosmic radiation bit-flips to rearrange memory
# until the list sorts itself. Checks periodically whether the miracle occurred.
# Seriously — this is a "real" algorithm as a theoretical joke.

from data import *
import time

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def miracle_sort(lista):
    lst = lista.copy()
    attempts = 0
    while not is_sorted(lst):
        attempts += 1
        print(f"Attempt {attempts}: no miracle yet, waiting for cosmic radiation...")
        time.sleep(1)
        if attempts >= 10:
            print("Miracle did not happen. The universe refuses to cooperate.")
            return lst
    print(f"MIRACLE! List sorted after {attempts} attempts!")
    return lst

if __name__ == "__main__":
    print(miracle_sort(losowa))
