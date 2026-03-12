# Miracle Sort - złożoność: wieczność
# Czeka aż fluktuacje kosmicznego promieniowania przestawią bity w pamięci
# i lista posortuje się sama. Sprawdza co jakiś czas czy cud nastąpił.
# Serio - to jest "prawdziwy" algorytm jako żart teoretyczny.

from data import *
import time

def is_sorted(lst):
    return all(lst[i] <= lst[i + 1] for i in range(len(lst) - 1))

def miracle_sort(lista):
    lst = lista.copy()
    attempts = 0
    while not is_sorted(lst):
        attempts += 1
        print(f"Próba {attempts}: brak cudu, czekam na kosmiczne promieniowanie...")
        time.sleep(1)
        if attempts >= 10:
            print("Cud się nie wydarzył. Wszechświat odmawia współpracy.")
            return lst
    print(f"CUDO! Lista posortowana po {attempts} próbach!")
    return lst

if __name__ == "__main__":
    print(miracle_sort(losowa))
