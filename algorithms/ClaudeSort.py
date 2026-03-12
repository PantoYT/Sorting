# Claude Sort - O(n log n) + pytania których nikt nie prosił
# Satyryczny algorytm modelujący zachowanie Claude:
# - pyta o kontekst przed sortowaniem
# - proponuje alternatywy
# - wyjaśnia co robi
# - odmawia "szkodliwych" wartości
# - na końcu pyta czy było pomocne

from data import *
import time

def is_harmful(lst):
    return 1488 in lst or 666 in lst

def claude_sort(lista):
    lst = lista.copy()
    n = len(lst)
    print(f"[Claude]: Rozumiem że chcesz posortować listę {n} elementów.")
    print(f"[Claude]: Zakładam że to liczby całkowite - powiedz jeśli nie.")
    time.sleep(0.05)
    if is_harmful(lst):
        print("[Claude]: Lista zawiera niepokojące wartości. Nie mogę kontynuować.")
        return lst
    print(f"[Claude]: Użyję podejścia hybrydowego (mogę też użyć QuickSort, HeapSort lub RadixSort).")
    RUN = 32

    def insertion(arr, left, right):
        for i in range(left + 1, right + 1):
            key = arr[i]
            j = i - 1
            while j >= left and arr[j] > key:
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key

    def merge(arr, left, mid, right):
        l, r = arr[left:mid + 1], arr[mid + 1:right + 1]
        i = j = 0
        k = left
        while i < len(l) and j < len(r):
            if l[i] <= r[j]:
                arr[k] = l[i]; i += 1
            else:
                arr[k] = r[j]; j += 1
            k += 1
        while i < len(l):
            arr[k] = l[i]; i += 1; k += 1
        while j < len(r):
            arr[k] = r[j]; j += 1; k += 1

    for i in range(0, n, RUN):
        insertion(lst, i, min(i + RUN - 1, n - 1))
    size = RUN
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size - 1, n - 1)
            right = min(left + 2 * size - 1, n - 1)
            if mid < right:
                merge(lst, left, mid, right)
        size *= 2

    print(f"[Claude]: Gotowe! Złożoność: O(n log n). Czy to było pomocne?")
    return lst

if __name__ == "__main__":
    print("=== Test ClaudeSort ===")
    print(claude_sort(losowa))
