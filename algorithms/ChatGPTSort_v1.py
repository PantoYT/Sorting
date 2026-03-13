# ChatGPT Sort v1 - O(n log n) + 10% chance of hallucination
# Satirical algorithm modelling LLM behaviour:
# - confident even when wrong
# - refuses "dangerous" lists
# - has limited "context window" (CONTEXT_WINDOW = 8)
# - 10% chance of random element swap ("hallucination")

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
        print("  [ChatGPT]: I am confident this is correct ✓")

def chatgpt_sort(lista):
    lst = lista.copy()
    n = len(lst)
    print(f"[ChatGPT]: Of course! Sorting a {n}-element list is a great task.")
    print(f"[ChatGPT]: I will use the optimal O(n log n) algorithm...")
    time.sleep(0.1)
    if is_dangerous(lst):
        print("[ChatGPT]: I'm sorry, I cannot sort this list.")
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
    print(f"[ChatGPT]: Done! Is there anything else I can help with?")
    return lst

if __name__ == "__main__":
    print("=== Test ChatGPTSort ===")
    print(chatgpt_sort(losowa))
    print()
    print("=== Test with dangerous list ===")
    print(chatgpt_sort([666, 1, 2, 3]))
