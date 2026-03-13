# Smooth Sort - O(n log n), O(n) for nearly sorted
# HeapSort variant using a "Leonardo heap" based on Leonardo numbers
# (L(0)=1, L(1)=1, L(n)=L(n-1)+L(n-2)+1 = 1,1,3,5,9,15,25,41...)
# Particularly efficient on nearly-sorted data.
# Unstable | In-place
# Note: the full implementation is one of the hardest in sorting theory.
# This version uses a simplified heap based on the Leonardo sequence.

from data import *

LEO = [1, 1]
while LEO[-1] < 10**7:
    LEO.append(LEO[-1] + LEO[-2] + 1)

def _heapify(lst, lo, hi):
    root = lo
    while True:
        child = 2 * (root - lo) + 1 + lo
        if child > hi:
            break
        if child + 1 <= hi and lst[child] < lst[child + 1]:
            child += 1
        if lst[root] >= lst[child]:
            break
        lst[root], lst[child] = lst[child], lst[root]
        root = child

def smooth_sort(lista):
    lst = lista.copy()
    n = len(lst)
    # buduj kopce o rozmiarach Leonardo
    sizes = []
    i = 0
    while i < n:
        if len(sizes) >= 2 and sizes[-1] == sizes[-2] - 1:
            new_size = sizes[-2] + sizes[-1] + 1
            sizes.pop(); sizes.pop()
            sizes.append(new_size)
        elif sizes and sizes[-1] == 1:
            sizes.append(1)
        else:
            sizes.append(1)
        # heapify current block
        start = i - sizes[-1] + 1
        _heapify(lst, start, i)
        # fix heap property between blocks
        j = len(sizes) - 1
        pos = i
        while j > 0:
            prev_end = pos - sizes[j]
            if lst[prev_end] > lst[pos]:
                lst[prev_end], lst[pos] = lst[pos], lst[prev_end]
                pos = prev_end
                j -= 1
            else:
                break
        i += 1
    # ekstrakcja
    for i in range(n - 1, -1, -1):
        if sizes[-1] > 1:
            start = i - sizes[-1] + 1
            left_child = start + LEO[LEO.index(sizes[-1]) - 1] if sizes[-1] in LEO else start
            right_child = i - 1
            # rozbij kopiec na dwa podkopce
            old = sizes.pop()
            # approximate: find children sizes
            k = LEO.index(old) if old in LEO else -1
            if k >= 2:
                sizes.append(LEO[k - 1])
                sizes.append(LEO[k - 2])
                _heapify(lst, i - LEO[k - 2] - LEO[k - 1], i - LEO[k - 2] - 1)
                _heapify(lst, i - LEO[k - 2], i - 1)
            else:
                sizes.append(1)
        else:
            sizes.pop()
    return lst

if __name__ == "__main__":
    from data import losowa, prawie_posort, odwrocona, duplikaty
    for t in [losowa, prawie_posort, odwrocona, duplikaty]:
        print(smooth_sort(t) == sorted(t), smooth_sort(t))
