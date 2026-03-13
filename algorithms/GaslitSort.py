# Gaslit Sort - O(n²) but claims O(1)
# Sorts the list correctly (using insertion sort), then lies to your face
# about what it did. Denies any wrongdoing. Questions your memory.
# "I didn't sort anything, the list was always like this."
# Satirical | Actually correct | Psychologically damaging

from data import *
import time

_gaslit_log = []

def gaslit_sort(lista):
    global _gaslit_log
    lst = lista.copy()
    original = lista[:]
    n = len(lst)

    # actually sort it (insertion sort internally)
    for i in range(1, n):
        key = lst[i]
        j = i - 1
        while j >= 0 and lst[j] > key:
            lst[j + 1] = lst[j]
            j -= 1
        lst[j + 1] = key

    # now gaslight
    _gaslit_log.append(original)
    print(f"[GaslitSort]: I didn't change anything.")
    print(f"[GaslitSort]: The list was always {lst}.")
    print(f"[GaslitSort]: Are you sure you remember it correctly?")
    print(f"[GaslitSort]: O(1) complexity. I barely did anything.")
    time.sleep(0.01)
    return lst

if __name__ == "__main__":
    result = gaslit_sort(losowa)
    print(f"Result: {result}")
    print(f"Original: {losowa}")
    print("[GaslitSort]: See? Nothing changed.")
