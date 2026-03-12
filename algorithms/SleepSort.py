# Sleep Sort - O(max(lista)) czasowo
# Dla każdego elementu uruchamia wątek który śpi przez n * 0.01 sekund,
# potem dopisuje element do wyniku. Mniejsze liczby budzą się wcześniej.
# Działa tylko na liczbach dodatnich. Czas = wartość największego elementu * 0.01s.

from data import *
import threading
import time

def sleep_sort(lista):
    lst = lista.copy()
    result = []

    def worker(x):
        time.sleep(x * 0.01)
        result.append(x)

    threads = [threading.Thread(target=worker, args=(x,)) for x in lst]
    for t in threads:
        t.start()
    for t in threads:
        t.join()
    return result

if __name__ == "__main__":
    testy = [losowa, duplikaty, male_wartosci]
    for t in testy:
        print(sleep_sort(t))
