# Drop Merge Sort - O(n log n), O(n) for nearly sorted
# Identifies the longest sorted subsequence, extracts the rest ("dropped" elements),
# sorts the dropped elements, then merges back.
# Extremely fast on nearly-sorted data (drops very few elements).
# Stable | O(n) memory | Best case O(n) when already sorted

from data import *

def drop_merge_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst

    # find elements that are "out of place" (need to be dropped)
    kept = [lst[0]]
    dropped = []
    for i in range(1, n):
        if lst[i] >= kept[-1]:
            kept.append(lst[i])
        else:
            dropped.append(lst[i])

    if not dropped:
        return kept  # already sorted

    # sort dropped elements
    dropped_sorted = sorted(dropped)

    # merge kept (already sorted) with sorted dropped
    result = []
    i = j = 0
    while i < len(kept) and j < len(dropped_sorted):
        if kept[i] <= dropped_sorted[j]:
            result.append(kept[i]); i += 1
        else:
            result.append(dropped_sorted[j]); j += 1
    result.extend(kept[i:])
    result.extend(dropped_sorted[j:])
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(drop_merge_sort(t))
