"""
Wizualizacja algorytmów sortowania - modularny, zero hardcode.
Algorytmy animowane są rejestrowane w VISUAL_REGISTRY.
Dodaj własny generator kroków żeby rozszerzyć wizualizację.
"""
import sys, os, random, argparse
sys.path.insert(0, os.path.dirname(__file__))

try:
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import matplotlib.gridspec as gridspec
except ImportError:
    print("Brak matplotlib: pip install matplotlib")
    sys.exit(1)

# ── kolory ────────────────────────────────────────────────────────────────────
BG      = "#1E1E2E"
CLR_DEF = "#4C9BE8"
CLR_CMP = "#FF6B6B"
CLR_SRT = "#6BCB77"
CLR_PIV = "#FFD93D"
CLR_ACT = "#C77DFF"

# ── generatory kroków: yield (stan, [porównywane], [posortowane], label) ──────

def _bubble(lst):
    n = len(lst); a = lst[:]
    for i in range(n - 1):
        for j in range(n - i - 1):
            yield a[:], [j, j+1], [], f"Porównaj [{j}] i [{j+1}]"
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                yield a[:], [j, j+1], [], "Zamiana"
    yield a[:], [], list(range(n)), "Posortowane!"

def _selection(lst):
    n = len(lst); a = lst[:]
    for i in range(n):
        m = i
        for j in range(i+1, n):
            yield a[:], [m, j], list(range(i)), f"Szukam min, kandydat [{j}]"
            if a[j] < a[m]: m = j
        a[i], a[m] = a[m], a[i]
        yield a[:], [i], list(range(i+1)), f"Min → pozycja {i}"
    yield a[:], [], list(range(n)), "Posortowane!"

def _insertion(lst):
    n = len(lst); a = lst[:]
    for i in range(1, n):
        key = a[i]; j = i - 1
        yield a[:], [i], list(range(i)), f"Wstawiam a[{i}]={key}"
        while j >= 0 and a[j] > key:
            yield a[:], [j, j+1], list(range(i)), f"Przesuwam [{j}] w prawo"
            a[j+1] = a[j]; j -= 1
        a[j+1] = key
        yield a[:], [j+1], list(range(i+1)), "Wstawiono"
    yield a[:], [], list(range(n)), "Posortowane!"

def _quick(lst):
    steps = []; a = lst[:]
    def qsort(lo, hi):
        if lo >= hi: return
        pivot = a[hi]
        steps.append((a[:], [hi], [], f"Pivot = {pivot}"))
        i = lo - 1
        for j in range(lo, hi):
            steps.append((a[:], [j, hi], [], f"Porównaj {a[j]} z pivot {pivot}"))
            if a[j] <= pivot:
                i += 1; a[i], a[j] = a[j], a[i]
                if i != j: steps.append((a[:], [i, j], [], "Zamiana"))
        a[i+1], a[hi] = a[hi], a[i+1]
        steps.append((a[:], [i+1], [], f"Pivot na pozycji {i+1}"))
        qsort(lo, i); qsort(i+2, hi)
    qsort(0, len(a)-1)
    for s in steps: yield s
    yield a[:], [], list(range(len(a))), "Posortowane!"

def _merge(lst):
    steps = []; a = lst[:]
    def msort(l, r):
        if r - l <= 1: return
        m = (l + r) // 2
        msort(l, m); msort(m, r)
        left, right = a[l:m], a[m:r]
        i = j = 0; k = l
        while i < len(left) and j < len(right):
            steps.append((a[:], [l+i, m+j], [], f"Scalanie: {left[i]} vs {right[j]}"))
            if left[i] <= right[j]: a[k] = left[i]; i += 1
            else: a[k] = right[j]; j += 1
            k += 1
        while i < len(left): a[k] = left[i]; i += 1; k += 1
        while j < len(right): a[k] = right[j]; j += 1; k += 1
        steps.append((a[:], list(range(l, r)), [], f"Scalono [{l}:{r}]"))
    msort(0, len(a))
    for s in steps: yield s
    yield a[:], [], list(range(len(a))), "Posortowane!"

def _heap(lst):
    steps = []; a = lst[:]
    def heapify(n, i):
        lg = i; l = 2*i+1; r = 2*i+2
        if l < n and a[l] > a[lg]: lg = l
        if r < n and a[r] > a[lg]: lg = r
        if lg != i:
            steps.append((a[:], [i, lg], [], f"Heap: zamień {a[i]} ↔ {a[lg]}"))
            a[i], a[lg] = a[lg], a[i]
            heapify(n, lg)
    n = len(a)
    for i in range(n//2-1, -1, -1): heapify(n, i)
    for i in range(n-1, 0, -1):
        a[0], a[i] = a[i], a[0]
        steps.append((a[:], [0, i], list(range(i, n)), f"Wyciągnięto max → pos {i}"))
        heapify(i, 0)
    for s in steps: yield s
    yield a[:], [], list(range(n)), "Posortowane!"

def _shell(lst):
    a = lst[:]; n = len(a); gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            temp = a[i]; j = i
            yield a[:], [j, max(0,j-gap)], [], f"Gap={gap}, porównaj [{j}] i [{j-gap}]"
            while j >= gap and a[j-gap] > temp:
                a[j] = a[j-gap]; j -= gap
                yield a[:], [j], [], "Przesuń"
            a[j] = temp
        gap //= 2
    yield a[:], [], list(range(n)), "Posortowane!"

def _knuth(lst):
    """3-way QuickSort"""
    steps = []; a = lst[:]
    def sort3(lo, hi):
        if hi <= lo: return
        lt, gt = lo, hi; pivot = a[lo]; i = lo + 1
        steps.append((a[:], [lo], [], f"3-way pivot={pivot}"))
        while i <= gt:
            steps.append((a[:], [i], [], f"Klasyfikuj {a[i]}"))
            if a[i] < pivot:
                a[lt], a[i] = a[i], a[lt]; lt += 1; i += 1
            elif a[i] > pivot:
                a[i], a[gt] = a[gt], a[i]; gt -= 1
            else: i += 1
        steps.append((a[:], list(range(lt, gt+1)), [], f"= {pivot}: [{lt}..{gt}]"))
        sort3(lo, lt-1); sort3(gt+1, hi)
    sort3(0, len(a)-1)
    for s in steps: yield s
    yield a[:], [], list(range(len(a))), "Posortowane!"

def _exchange(lst):
    n = len(lst); a = lst[:]
    for i in range(n-1):
        for j in range(i+1, n):
            yield a[:], [i, j], list(range(i)), f"Porównaj a[{i}]={a[i]} vs a[{j}]={a[j]}"
            if a[i] > a[j]:
                a[i], a[j] = a[j], a[i]
                yield a[:], [i, j], list(range(i)), "Zamiana"
    yield a[:], [], list(range(n)), "Posortowane!"

def _counting(lst):
    a = lst[:]; n = len(a)
    mn, mx = min(a), max(a)
    cnt = [0] * (mx - mn + 1)
    for x in a:
        cnt[x-mn] += 1
        yield a[:], [], [], f"Liczę: a[{a.index(x)}]={x} → bucket[{x-mn}]={cnt[x-mn]}"
    result = []
    for i, c in enumerate(cnt):
        result.extend([i+mn]*c)
        if c: yield result + a[len(result):], list(range(len(result)-c, len(result))), [], f"Odtwarzam wartość {i+mn} ({c}x)"
    yield result, [], list(range(n)), "Posortowane!"

# ── rejestr wizualny ──────────────────────────────────────────────────────────
# Klucz = nazwa wyświetlana, wartość = generator funkcja
VISUAL_REGISTRY = {
    "Bubble Sort":     _bubble,
    "Selection Sort":  _selection,
    "Insertion Sort":  _insertion,
    "Quick Sort":      _quick,
    "Merge Sort":      _merge,
    "Heap Sort":       _heap,
    "Shell Sort":      _shell,
    "Knuth (3-way)":   _knuth,
    "Exchange Sort":   _exchange,
    "Counting Sort":   _counting,
}

def register_algorithm(name, generator_func):
    """Dodaj własny algorytm do wizualizacji. Patrz: VISUAL_REGISTRY."""
    VISUAL_REGISTRY[name] = generator_func

# ── rendering ─────────────────────────────────────────────────────────────────

def visualize(name, data, interval=40, save_path=None):
    gen_func = VISUAL_REGISTRY[name]
    steps = list(gen_func(data[:]))
    n = len(data)

    fig = plt.figure(figsize=(13, 6), facecolor=BG)
    gs = gridspec.GridSpec(1, 2, width_ratios=[4, 1], wspace=0.08)
    ax  = fig.add_subplot(gs[0])
    axr = fig.add_subplot(gs[1])

    for a in [ax, axr]:
        a.set_facecolor(BG)
        for sp in a.spines.values(): sp.set_edgecolor("#333")

    ax.set_title(name, color="white", fontsize=15, pad=10, fontweight="bold")
    ax.tick_params(colors="#888"); axr.axis("off")

    bars = ax.bar(range(n), steps[0][0], color=CLR_DEF,
                  edgecolor=BG, linewidth=0.5)
    ax.set_xlim(-0.5, n-0.5)
    ax.set_ylim(0, max(data)*1.12)

    info_box = axr.text(0.05, 0.95, "", transform=axr.transAxes,
                        color="white", fontsize=9, va="top", family="monospace",
                        bbox=dict(boxstyle="round,pad=0.5", facecolor="#2a2a3e", edgecolor="#555"))

    def update(frame):
        if frame >= len(steps): return bars,
        state, cmp, srt, label = steps[frame]
        for i, bar in enumerate(bars):
            if i in srt:   bar.set_color(CLR_SRT)
            elif i in cmp: bar.set_color(CLR_CMP)
            else:          bar.set_color(CLR_DEF)
            bar.set_height(state[i])
        pct = (frame+1)/len(steps)*100
        info_box.set_text(
            f"Krok {frame+1}/{len(steps)}\n"
            f"{pct:.0f}% ukończone\n\n"
            f"{label}\n\n"
            f"n = {n}\n"
            f"cmp = {len(cmp)}\n"
            f"done = {len(srt)}"
        )
        return bars,

    ani = animation.FuncAnimation(fig, update, frames=len(steps),
                                   interval=interval, blit=False, repeat=False)
    if save_path:
        ani.save(save_path, writer="pillow", fps=1000//interval)
        print(f"Zapisano: {save_path}")
    else:
        plt.tight_layout()
        plt.show()
    plt.close()
    return ani

def visualize_compare(names, data, interval=40):
    """Animuj kilka algorytmów obok siebie na tych samych danych."""
    n_algos = len(names)
    fig, axes = plt.subplots(1, n_algos, figsize=(5*n_algos, 5), facecolor=BG)
    if n_algos == 1: axes = [axes]
    for ax in axes:
        ax.set_facecolor(BG)
        for sp in ax.spines.values(): sp.set_edgecolor("#333")

    all_steps = [list(VISUAL_REGISTRY[name](data[:])) for name in names]
    max_steps  = max(len(s) for s in all_steps)
    all_bars   = []
    n = len(data)

    for idx, (ax, name, steps) in enumerate(zip(axes, names, all_steps)):
        ax.set_title(name, color="white", fontsize=11, pad=8)
        ax.tick_params(colors="#666")
        bars = ax.bar(range(n), steps[0][0], color=CLR_DEF, edgecolor=BG, linewidth=0.4)
        ax.set_xlim(-0.5, n-0.5)
        ax.set_ylim(0, max(data)*1.1)
        all_bars.append(bars)

    def update(frame):
        for bars, steps in zip(all_bars, all_steps):
            f = min(frame, len(steps)-1)
            state, cmp, srt, _ = steps[f]
            for i, bar in enumerate(bars):
                if i in srt:   bar.set_color(CLR_SRT)
                elif i in cmp: bar.set_color(CLR_CMP)
                else:          bar.set_color(CLR_DEF)
                bar.set_height(state[i])
        return [b for bars in all_bars for b in bars]

    fig.suptitle("Porównanie algorytmów", color="white", fontsize=13)
    ani = animation.FuncAnimation(fig, update, frames=max_steps,
                                   interval=interval, blit=False, repeat=False)
    plt.tight_layout()
    plt.show()
    return ani

# ── menu ──────────────────────────────────────────────────────────────────────

def menu():
    names = list(VISUAL_REGISTRY.keys())
    sizes = [10, 20, 30, 50]

    print("\n╔══════════════════════════════════════╗")
    print("║   WIZUALIZACJA SORTOWANIA            ║")
    print("╚══════════════════════════════════════╝")
    print("\nAlgorytmy:")
    for i, n in enumerate(names, 1):
        print(f"  {i:>2}. {n}")
    print(f"  {len(names)+1:>2}. Porównanie wszystkich (obok siebie)")
    print(f"   0. Wyjście")

    print("\nRozmiar listy:")
    for i, s in enumerate(sizes, 1):
        print(f"  {i}. {s} elementów")

    try:
        algo_in = input("\nWybierz algorytm: ").strip()
        size_in = input("Wybierz rozmiar (1-4, Enter=2): ").strip() or "2"
        speed_in = input("Prędkość ms/krok (Enter=40ms): ").strip() or "40"
    except (KeyboardInterrupt, EOFError):
        return

    try:
        algo_choice = int(algo_in)
        size_idx    = max(0, min(3, int(size_in) - 1))
        speed       = max(10, int(speed_in))
    except ValueError:
        print("Nieprawidłowy wybór.")
        return

    if algo_choice == 0:
        return
    size = sizes[size_idx]
    data = random.sample(range(1, size+1), size)
    print(f"\nDane: {data}\n")

    if algo_choice == len(names) + 1:
        # porównaj wszystkie
        visualize_compare(names, data, interval=speed)
    elif 1 <= algo_choice <= len(names):
        visualize(names[algo_choice-1], data, interval=speed)
    else:
        print("Nieprawidłowy wybór.")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Wizualizacja sortowania")
    parser.add_argument("algo", nargs="?", help="Nazwa algorytmu (opcjonalnie)")
    parser.add_argument("--size", "-s", type=int, default=20)
    parser.add_argument("--speed", type=int, default=40, help="ms/krok")
    parser.add_argument("--compare", "-c", action="store_true",
                        help="Porównaj wszystkie algorytmy obok siebie")
    args = parser.parse_args()

    if args.algo:
        matches = [n for n in VISUAL_REGISTRY if args.algo.lower() in n.lower()]
        if not matches:
            print(f"Nie znaleziono: {args.algo}")
            print(f"Dostępne: {list(VISUAL_REGISTRY.keys())}")
            sys.exit(1)
        data = random.sample(range(1, args.size+1), args.size)
        if args.compare:
            visualize_compare(matches, data, interval=args.speed)
        else:
            visualize(matches[0], data, interval=args.speed)
    elif args.compare:
        data = random.sample(range(1, args.size+1), args.size)
        visualize_compare(list(VISUAL_REGISTRY.keys()), data, interval=args.speed)
    else:
        menu()
