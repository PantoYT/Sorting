# Stalin Sort - O(n)
# Przechodzi przez listę raz. Każdy element który jest mniejszy od poprzedniego
# zostaje "usunięty" (rozstrzelany). Wynik zawsze posortowany, ale dane giną.
# "Stabilny" | In-place | 100% skuteczny, 0% użyteczny

from data import *

def stalin_sort(lista):
    lst = lista.copy()
    result = [lst[0]]
    for x in lst[1:]:
        if x >= result[-1]:
            result.append(x)
    return result

if __name__ == "__main__":
    testy = [losowa, odwrocona, duplikaty]
    for t in testy:
        print(stalin_sort(t))
