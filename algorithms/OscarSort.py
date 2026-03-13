# Oscar Sort - O(n²) | Satirical
# Named after Oscar the Grouch (lives in a trash can, doesn't want to be sorted).
# Complains loudly about every comparison, tries to avoid sorting,
# eventually gives in and does bubble sort while grumbling.
# Correctly sorts | Satirical | Runtime includes complaint overhead

from data import *
import time

COMPLAINTS = [
    "Ugh, do I HAVE to?",
    "This is the WORST.",
    "I liked it better messy.",
    "You call THIS a job?",
    "Go away. I'm busy being unsorted.",
    "FINE. But I'm not happy about it.",
    "Can't you just leave it alone?",
]

def oscar_sort(lista):
    lst = lista.copy()
    n = len(lst)
    import random
    print(f"[OscarSort]: {random.choice(COMPLAINTS)}")
    time.sleep(0.02)
    # does bubble sort while complaining
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]
    print(f"[OscarSort]: There. Happy now? Scram.")
    return lst

if __name__ == "__main__":
    print(oscar_sort(losowa))
