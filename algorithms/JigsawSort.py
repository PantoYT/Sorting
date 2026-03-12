# Jigsaw Sort - O(n²)
# Sortuje "puzzlowo" - dzieli listę na kawałki, sortuje każdy,
# potem scala je jak układankę dopasowując krawędzie (ostatni el. bloku <= pierwszy el. następnego).
# Jeśli kawałki nie pasują, zamienia sąsiadujące elementy na granicy i powtarza.
# Stabilny | O(n) pamięci | Oryginalny algorytm edukcyjny

from data import *

def jigsaw_sort(lista):
    lst = lista.copy()
    n = len(lst)
    if n <= 1:
        return lst
    block = max(2, n // 4)
    # sortuj bloki
    for i in range(0, n, block):
        end = min(i + block, n)
        lst[i:end] = sorted(lst[i:end])
    # scalaj dopasowując "krawędzie" dopóki całość nie jest posortowana
    changed = True
    while changed:
        changed = False
        for i in range(0, n, block):
            end = min(i + block, n)
            next_start = end
            next_end = min(next_start + block, n)
            if next_end <= n and next_start < n:
                if lst[end - 1] > lst[next_start]:
                    segment = lst[i:next_end]
                    segment.sort()
                    lst[i:next_end] = segment
                    changed = True
    return lst

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(jigsaw_sort(t))
