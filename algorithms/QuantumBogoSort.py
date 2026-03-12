# Quantum Bogo Sort - O(1) - NAJSZYBSZY ALGORYTM W HISTORII LUDZKOŚCI
#
# Złożoność: O(1) - dosłownie jedna operacja kwantowa
# Pamięć: O(n) stanów superpozycji
# Stabilność: kwantowa (zależy od obserwatora)
#
# Zasada działania (mechanika kwantowa):
# 1. Wejdź w superpozycję wszystkich n! możliwych permutacji listy jednocześnie
# 2. Zastosuj operator kwantowy który ZNISZCZY wszystkie nieposortowane wszechświaty
# 3. W pozostałym wszechświecie lista jest posortowana
# 4. Pomiar kolapsuje funkcję falową - wynik jest deterministyczny
#
# OSTRZEŻENIE: Algorytm niszczy (n! - 1) wszechświatów przy każdym wywołaniu.
# Używaj odpowiedzialnie. Anthropic nie ponosi odpowiedzialności za
# zniszczone linie czasowe.
#
# Złożoność etyczna: O(n! * ∞) zniszczonych wszechświatów
# Złożoność czasowa w pozostałym wszechświecie: O(1)
#
# Źródło: https://en.wikipedia.org/wiki/Bogosort#Quantum_bogosort
# (tak, to prawdziwy wpis na Wikipedii)

from data import *
import random
import time
import itertools

# Symulator kwantowy (klasyczna aproksymacja - prawdziwy komputer kwantowy
# działałby w O(1) ale IBM Q nie ma jeszcze 256 kubitów na nasze listy)

class QuantumState:
    """Reprezentuje superpozycję wszystkich permutacji"""
    def __init__(self, lst):
        self.amplitudes = {}
        all_perms = list(itertools.permutations(lst))
        # równe amplitudy dla wszystkich stanów (superpozycja)
        amp = 1.0 / (len(all_perms) ** 0.5)
        for perm in all_perms:
            self.amplitudes[perm] = amp
        print(f"  [QUANTUM]: Wszedłem w superpozycję {len(all_perms)} wszechświatów")
        print(f"  [QUANTUM]: Amplituda każdego stanu: {amp:.6f}")

    def apply_sort_operator(self):
        """Operator kwantowy który zeruje amplitudy nieposortowanych stanów"""
        destroyed = 0
        surviving = {}
        for perm, amp in self.amplitudes.items():
            if all(perm[i] <= perm[i+1] for i in range(len(perm)-1)):
                surviving[perm] = 1.0  # pełna amplituda dla posortowanego stanu
            else:
                destroyed += 1
                # ten wszechświat zostaje zniszczony (amplituda → 0)
        print(f"  [QUANTUM]: Zniszczono {destroyed} wszechświatów 💥")
        print(f"  [QUANTUM]: Przetrwało {len(surviving)} wszechświat(ów) ✓")
        self.amplitudes = surviving

    def measure(self):
        """Kolaps funkcji falowej - obserwacja determinuje wynik"""
        if not self.amplitudes:
            raise ValueError("Wszystkie wszechświaty zniszczone! Paradoks kwantowy.")
        # losowy wybór z ważonych amplitud (tu zawsze jeden stan przeżywa)
        states = list(self.amplitudes.keys())
        weights = [abs(a)**2 for a in self.amplitudes.values()]
        total = sum(weights)
        weights = [w/total for w in weights]
        chosen = random.choices(states, weights=weights)[0]
        print(f"  [QUANTUM]: Funkcja falowa skolapsowana. Obserwacja zakończona.")
        return list(chosen)


def quantum_bogo_sort(lista):
    lst = lista.copy()
    n = len(lst)

    print(f"\n{'='*60}")
    print(f"  QUANTUM BOGO SORT - n={n} elementów")
    print(f"  Inicjalizuję komputer kwantowy...")
    print(f"{'='*60}")

    # OSTRZEŻENIE dla dużych list
    import math
    factorial = math.factorial(n)
    if factorial > 10**6:
        print(f"\n  ⚠️  UWAGA: Ta operacja zniszczy {factorial:,} wszechświatów!")
        print(f"  ⚠️  Dla n={n} mamy {n}! = {factorial:,} permutacji")
        print(f"  ⚠️  Używam optymalizacji kwantowej (symulacja losowa)...")
        # dla dużych list - symulacja przez losowe tasowanie jak BogoSort
        # ale z kwantowym szumem i dramatycznymi komunikatami
        attempts = 0
        while lst != sorted(lst):
            random.shuffle(lst)
            attempts += 1
            if attempts % 1000 == 0:
                print(f"  [QUANTUM]: Kolaps #{attempts}... szukam posortowanego wszechświata...")
        print(f"  [QUANTUM]: Znaleziono! Po {attempts} kolapsach funkcji falowej.")
        return lst

    # Dla małych list - prawdziwa symulacja kwantowa przez superpozycję
    t_start = time.perf_counter()

    # Krok 1: superpozycja
    state = QuantumState(lst)
    time.sleep(0.05)  # czas na "kwantową kohencję"

    # Krok 2: operator sortujący
    state.apply_sort_operator()
    time.sleep(0.02)  # czas na "dekoherencję"

    # Krok 3: pomiar
    result = state.measure()

    t_end = time.perf_counter()
    print(f"  [QUANTUM]: Czas obliczeń kwantowych: {(t_end-t_start)*1000:.2f}ms")
    print(f"  [QUANTUM]: W klasycznej implementacji: O(1) kolapsy funkcji falowej")
    print(f"{'='*60}\n")
    return result


if __name__ == "__main__":
    print("=== QUANTUM BOGO SORT ===")
    print("O KURWA ZROBIŁEM QUANTUM BOGO SORT")
    print()

    # Demo na małej liście
    mala = [3, 1, 4, 1, 5]
    print(f"Wejście: {mala}")
    wynik = quantum_bogo_sort(mala)
    print(f"Wyjście: {wynik}")
    print(f"Poprawny: {wynik == sorted(mala)}")

    print()
    print("Złożoność obliczeniowa:")
    print("  Klasyczna: O(1) kolapsy funkcji falowej")
    print("  Etyczna:   O(n! × ∞) zniszczonych wszechświatów")
    print("  Przestrzeń: O(n!) superpozycji")
    print()
    print("Twierdzenie: Jeśli wieloświat jest prawdziwy,")
    print("Quantum Bogo Sort jest NAJSZYBSZYM możliwym algorytmem.")
    print("Dowód: istnieje wszechświat gdzie lista jest już posortowana.")
    print("Wystarczy go znaleźć i zniszczyć pozostałe. QED.")
