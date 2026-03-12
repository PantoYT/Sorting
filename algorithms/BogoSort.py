# Bogo Sort - O(n * n!) avg, może nigdy nie skończyć
# Losowo tasuje listę dopóki nie jest posortowana.
# Teoretycznie może nigdy nie skończyć (nieskończona złożoność worst case).
# Niestabilny | In-place | Absolutnie bezużyteczny, legendarny

from data import *
import random

def bogo_sort(lista):
    lst = lista.copy()
    while lst != sorted(lst):
        random.shuffle(lst)
    return lst

if __name__ == "__main__":
    # tylko mała lista!
    print(bogo_sort(losowa))
