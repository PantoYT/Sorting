# Stalin Sort - O(n)
# Iterates through the list once. Any element smaller than the previous one
# is "removed" (shot). Result is always sorted, but data is lost.
# "Stable" | In-place | 100% effective, 0% useful

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
