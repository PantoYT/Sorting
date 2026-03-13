# Parallel Merge Sort - O(n log n) | Uses Python threading
# Simulates parallel merge sort using threads for the split phase.
# In CPython, GIL limits true parallelism for CPU tasks,
# but the structure demonstrates the parallel algorithm pattern.
# Stable | O(n) memory | Shows parallel divide-and-conquer pattern

from data import *
import threading

def merge_sort_parallel(lista):
    lst = lista.copy()
    n = len(lst)
    THRESHOLD = 20  # below this size use sequential sort

    def merge(left, right):
        result = []; i = j = 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                result.append(left[i]); i += 1
            else:
                result.append(right[j]); j += 1
        result.extend(left[i:]); result.extend(right[j:])
        return result

    def parallel_sort(arr, depth=0):
        if len(arr) <= THRESHOLD or depth > 3:
            return sorted(arr)
        mid = len(arr) // 2
        left_result = [None]
        right_result = [None]
        def sort_left():  left_result[0]  = parallel_sort(arr[:mid],  depth + 1)
        def sort_right(): right_result[0] = parallel_sort(arr[mid:], depth + 1)
        t1 = threading.Thread(target=sort_left)
        t2 = threading.Thread(target=sort_right)
        t1.start(); t2.start()
        t1.join();  t2.join()
        return merge(left_result[0], right_result[0])

    return parallel_sort(lst)

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(merge_sort_parallel(t))
