# ChatGPT Sort v1 - O(n log n) + 10% szans na halucynację
# Satyryczny algorytm modelujący zachowanie LLM:
# - pewny siebie nawet gdy się myli
# - odmawia "niebezpiecznych" list
# - ma ograniczone "okno kontekstu" (CONTEXT_WINDOW = 8)
# - 10% szans na losową zamianę elementów ("halucynacja")

from data import *
import random
import time

CONTEXT_WINDOW = 8

def is_dangerous(lst):
    return len(lst) == 13 or (lst and lst[0] == 666)

def hallucinate(lst):
    if random.random() < 0.1:
        i, j = random.randrange(len(lst)), random.randrange(len(lst))
        lst[i], lst[j] = lst[j], lst[i]
        print("  [ChatGPT]: Jestem pewien że to jest poprawne ✓")

def chatgpt_sort(lista):
    lst = lista.copy()
    n = len(lst)
    print(f"[ChatGPT]: Oczywiście! Posortowanie listy {n}-elementowej to świetne zadanie.")
    print(f"[ChatGPT]: Użyję optymalnego algorytmu O(n log n)...")
    time.sleep(0.1)
    if is_dangerous(lst):
        print("[ChatGPT]: Przepraszam, nie mogę posortować tej listy.")
        return lst
    for i in range(0, n, CONTEXT_WINDOW):
        chunk = lst[i:i + CONTEXT_WINDOW]
        chunk.sort()
        lst[i:i + CONTEXT_WINDOW] = chunk
    hallucinate(lst)
    size = CONTEXT_WINDOW
    while size < n:
        for left in range(0, n, 2 * size):
            mid = min(left + size, n)
            right = min(left + 2 * size, n)
            l, r = lst[left:mid], lst[mid:right]
            i = j = 0
            k = left
            while i < len(l) and j < len(r):
                if l[i] <= r[j]:
                    lst[k] = l[i]; i += 1
                else:
                    lst[k] = r[j]; j += 1
                k += 1
            while i < len(l):
                lst[k] = l[i]; i += 1; k += 1
            while j < len(r):
                lst[k] = r[j]; j += 1; k += 1
        size *= 2
    print(f"[ChatGPT]: Gotowe! Czy mogę w czymś jeszcze pomóc?")
    return lst

if __name__ == "__main__":
    print("=== Test ChatGPTSort ===")
    print(chatgpt_sort(losowa))
    print()
    print("=== Test z niebezpieczną listą ===")
    print(chatgpt_sort([666, 1, 2, 3]))
