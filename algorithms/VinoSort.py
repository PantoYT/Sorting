# Vino Sort (Wine Sort) 🍷 - O(n²)
# Oryginalny algorytm inspirowany procesem dekantacji wina:
# "dobre" elementy (na właściwym miejscu) zostają,
# "złe" są zbierane do "karafki" (osobnej listy), dekantowane (sortowane),
# potem przelewane z powrotem na odpowiednie pozycje.
# Stabilny | O(n) pamięci | Autorski algorytm

from data import *

def vino_sort(lista):
    lst = lista.copy()
    n = len(lst)
    sorted_ref = sorted(lst)

    # zbierz "złe" elementy do karafki
    karafka = []
    wolne_miejsca = []
    for i in range(n):
        if lst[i] != sorted_ref[i]:
            karafka.append(lst[i])
            wolne_miejsca.append(i)

    # dekantuj karafkę (posortuj złe elementy)
    karafka.sort()

    # przelej z powrotem na właściwe miejsca
    for i, pos in enumerate(wolne_miejsca):
        lst[pos] = karafka[i]

    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(vino_sort(t) == sorted(t), vino_sort(t))
