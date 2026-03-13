# Lazy Sort - O(n log n) but delays work as long as possible
# Wraps the input in a lazy evaluator that only sorts when you actually
# access elements. The sort happens on first access, then is cached.
# Classic functional programming / lazy evaluation pattern.
# Stable | O(n) memory | Useful when you might not need the sorted result

from data import *

class LazySortedList:
    """A list that sorts itself only when accessed."""
    def __init__(self, data):
        self._data = data[:]
        self._sorted = None

    def _ensure_sorted(self):
        if self._sorted is None:
            self._sorted = sorted(self._data)

    def __getitem__(self, idx):
        self._ensure_sorted()
        return self._sorted[idx]

    def __len__(self):
        return len(self._data)

    def to_list(self):
        self._ensure_sorted()
        return self._sorted[:]

def lazy_sort(lista):
    lst = lista.copy()
    lazy = LazySortedList(lst)
    # accessing it forces the sort
    return lazy.to_list()

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(lazy_sort(t))
