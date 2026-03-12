"""
Benchmark algorytmów sortowania - modularny, zero hardcode.
Algorytmy są wykrywane automatycznie z folderu algorithms/.
Dodaj nowy plik Sort -> pojawia się w benchmarku automatycznie.

Użycie:
    python benchmark.py                  # pełny benchmark
    python benchmark.py --filter Quick   # tylko algorytmy zawierające "Quick"
    python benchmark.py --top 10         # tylko top 10 najszybszych
"""
import sys, os, time, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from data import losowa, prawie_posort, odwrocona, duplikaty, duza, duza_losowa
from algorithms import REGISTRY

# ── konfiguracja ─────────────────────────────────────────────────────────────

# Pomijamy na dużych zestawach (zbyt wolne)
SKIP_LARGE = {
    "BubbleSort", "SelectionSort", "GnomeSort", "OddEvenSort", "CocktailShakerSort",
    "PancakeSort", "BurntPancakeSort", "LibrarySort", "DrunkSort", "PopCornSort",
    "NaiveSort", "ChatGPTSort_v1", "ChatGPTSort_v2", "StoogeSort",
    "BogoSort", "BogoBogoSort", "SlowSort",
}

# Pomijamy całkowicie (interaktywne / nigdy się nie kończą)
SKIP_ALL = {"MiracleSort", "SleepSort", "BogoBogoSort"}

# Losowe/satyryczne - nie weryfikujemy poprawności (oznaczamy ~)
NO_VERIFY = {
    "DrunkSort", "StalinSort", "ChatGPTSort_v1", "ChatGPTSort_v2",
    "ClaudeSort", "MiracleSort", "QuantumBogoSort",
}

# Specjalne małe dane dla algorytmów które nie mogą dostać dużych list
SPECIAL_DATA = {
    "QuantumBogoSort": ([3, 1, 4, 2, 5], "Kwantowe(5)"),
    "BogoSort":        ([5, 3, 1, 4, 2], "Bogo(5)"),
    "SlowSort":        ([7, 3, 1, 8, 2, 9, 4, 6, 5, 10], "Slow(10)"),
    "StoogeSort":      ([7, 3, 1, 8, 2, 9, 4, 6, 5, 10], "Stooge(10)"),
}

ZESTAWY_MALE = {
    "Losowa(7)":        losowa,
    "PrawiePosort(10)": prawie_posort,
    "Odwrocona(10)":    odwrocona,
    "Duplikaty(10)":    duplikaty,
}
ZESTAWY_DUZE = {
    "Duza(100)":        duza,
    "DuzaLosowa(100)":  duza_losowa,
}
ZESTAWY_WSZYSTKIE = {**ZESTAWY_MALE, **ZESTAWY_DUZE}

# ── pomiar ────────────────────────────────────────────────────────────────────

def zmierz(func, lista, powtorzenia=3):
    wynik = None
    czasy = []
    for _ in range(powtorzenia):
        t0 = time.perf_counter()
        wynik = func(lista)
        czasy.append(time.perf_counter() - t0)
    return min(czasy), wynik

def weryfikuj(wynik, lista):
    return wynik == sorted(lista)

def fmt(t):
    if t < 1e-6: return f"{t*1e9:.0f}ns"
    if t < 1e-3: return f"{t*1e6:.1f}µs"
    if t < 1:    return f"{t*1e3:.2f}ms"
    return f"{t:.2f}s"

# ── main ──────────────────────────────────────────────────────────────────────

def run_benchmark(filter_name=None):
    algos = {k: v for k, v in sorted(REGISTRY.items())
             if k not in SKIP_ALL
             and (filter_name is None or filter_name.lower() in k.lower())}

    col_w = 16
    print("=" * 107)
    print(f"  BENCHMARK ALGORYTMÓW SORTOWANIA  •  {len(algos)} algorytmów  •  auto-discovery z algorithms/")
    print("=" * 107)
    header = f"{'Algorytm':<26}"
    for n in ZESTAWY_WSZYSTKIE:
        header += f"{n:>{col_w}}"
    header += f"{'✓':>6}"
    print(header)
    print("-" * 107)

    wyniki = []
    for nazwa, func in algos.items():
        is_special = nazwa in SPECIAL_DATA
        is_no_verify = nazwa in NO_VERIFY

        if is_special:
            special_lst, special_label = SPECIAL_DATA[nazwa]
            try:
                t, wynik = zmierz(func, special_lst, powtorzenia=1)
                ok = is_no_verify or weryfikuj(wynik, special_lst)
                row = f"{nazwa:<26}" + f"{'':>{col_w}}"*5 + f"{fmt(t):>{col_w}}"
            except Exception:
                ok = False
                row = f"{nazwa:<26}" + f"{'ERR':>{col_w}}"*6
            row += f"{'~' if is_no_verify else ('✓' if ok else '✗'):>6}"
            print(row)
            wyniki.append((nazwa, t if is_special else 0, ok, is_no_verify))
            continue

        row = f"{nazwa:<26}"
        poprawny = True
        suma = 0.0
        for zestaw_nazwa, lista in ZESTAWY_WSZYSTKIE.items():
            is_duza = zestaw_nazwa in ZESTAWY_DUZE
            if is_duza and nazwa in SKIP_LARGE:
                row += f"{'skip':>{col_w}}"; continue
            try:
                t, wynik = zmierz(func, lista)
                suma += t
                if not is_no_verify and not weryfikuj(wynik, lista):
                    poprawny = False
                row += f"{fmt(t):>{col_w}}"
            except Exception:
                row += f"{'ERR':>{col_w}}"; poprawny = False
        row += f"{'~' if is_no_verify else ('✓' if poprawny else '✗'):>6}"
        print(row)
        wyniki.append((nazwa, suma, poprawny, is_no_verify))

    print("=" * 107)

    # ranking
    ranked = sorted(
        [(n, t) for n, t, ok, skip_v in wyniki if ok and not skip_v and t > 0],
        key=lambda x: x[1]
    )
    max_t = ranked[-1][1] if ranked else 1
    print(f"\nRANKING — od najszybszego (n={len(ranked)} algorytmów z pełną weryfikacją):")
    print("─" * 58)
    for i, (n, t) in enumerate(ranked, 1):
        bar = "█" * max(1, int(t / max_t * 25))
        print(f"  {i:>2}. {n:<28} {fmt(t):>8}  {bar}")

    bledy = [n for n, _, ok, sv in wyniki if not ok and not sv]
    satyry = [n for n, _, _, sv in wyniki if sv]
    if bledy:
        print(f"\n✗ BŁĘDY ({len(bledy)}): {', '.join(bledy)}")
    if satyry:
        print(f"\n~ SATYRYCZNE/LOSOWE (nie weryfikowane): {', '.join(satyry)}")

    first = set(n[0].upper() for n in REGISTRY)
    missing = sorted(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - first)
    covered = sorted(first)
    print(f"\nLITERY: {len(covered)}/26 pokrytych  |  łącznie {len(REGISTRY)} algorytmów")
    print("  " + " ".join(f"\033[92m{l}\033[0m" if l in first else f"\033[91m{l}\033[0m"
                           for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"))
    if missing:
        print(f"  Brakuje: {' '.join(missing)}  ← weź PR i domknij alfabet!")
    else:
        print("  ✓ Wszystkie 26 liter pokryte!")

if __name__ == "__main__":
    p = argparse.ArgumentParser()
    p.add_argument("--filter", "-f", default=None, help="filtruj po nazwie")
    args = p.parse_args()
    run_benchmark(filter_name=args.filter)
