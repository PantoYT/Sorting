"""
Sorting Algorithm Benchmark — modular, zero hardcoding, RAM-efficient.
Algorithms are auto-discovered from algorithms/.

Usage:
    python benchmark.py                         # full benchmark
    python benchmark.py -f Quick                # filter by name
    python benchmark.py -a BubbleSort,TimSort   # specific algorithms
    python benchmark.py --list                  # list all algorithms
    python benchmark.py --top 10                # show top N
    python benchmark.py --size 50               # custom test size
"""
import sys, os, time, argparse, gc
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from algorithms import REGISTRY

# ── Configuration ────────────────────────────────────────────────────────────

# Skip on large datasets (too slow to be useful)
SKIP_LARGE: set[str] = {
    "BubbleSort", "SelectionSort", "GnomeSort", "OddEvenSort",
    "CocktailShakerSort", "PancakeSort", "BurntPancakeSort", "LibrarySort",
    "DrunkSort", "PopCornSort", "NaiveSort", "EfficientBogoSort",
    "ReverseBubbleSort", "ExchangeSort", "PancakeNumberSort",
    "EvenOddTranspositionSort", "ShuffleSort", "EscapeSort", "OscarSort",
    "ChatGPTSort_v1", "ChatGPTSort_v2",
}

# Never run in automated benchmark (interactive / infinite / destructive)
SKIP_ALL: set[str] = {
    "MiracleSort", "SleepSort", "BogoBogoSort",  "AntiBubbleSort",
}

# Don't verify correctness (random / satirical / destructive by design)
NO_VERIFY: set[str] = {
    "DrunkSort", "StalinSort", "ChatGPTSort_v1", "ChatGPTSort_v2",
    "ClaudeSort", "GaslitSort", "CorruptionSort", "OscarSort",
    "McCarthySort", "AntiBubbleSort", "QuantumBogoSort", "ShuffleSort",
    "EscapeSort",
}

# Algorithms that need tiny datasets (computational explosion)
SPECIAL_DATA: dict[str, tuple[list, str]] = {
    "QuantumBogoSort": ([3, 1, 4, 2, 5],       "Quantum(5)"),
    "BogoSort":        ([5, 3, 1, 4, 2],        "Bogo(5)"),
    "SlowSort":        ([7,3,1,8,2,9,4,6,5,10], "Slow(10)"),
    "StoogeSort":      ([7,3,1,8,2,9,4,6,5,10], "Stooge(10)"),
    "McCarthySort":    ([5, 3, 1, 4, 2],        "McCarthy(5)"),
    "BogoBogoSort":    ([3, 1, 2],              "BogoBogo(3)"),
}

# ── Dataset generation ───────────────────────────────────────────────────────

def make_datasets(size: int = 100) -> dict[str, list]:
    import random
    small = min(size, 10)
    tiny  = min(size, 7)
    return {
        f"Random({tiny})":        random.sample(range(1, tiny * 10), tiny),
        f"NearSorted({small})":   sorted(random.sample(range(1, small*3), small),
                                         key=lambda x: x + random.randint(-1,1)),
        f"Reversed({small})":     list(range(small, 0, -1)),
        f"Duplicates({small})":   [random.randint(1, small//2) for _ in range(small)],
        f"Large({size})":         list(range(size, 0, -1)),
        f"LargeRandom({size})":   random.sample(range(1, size * 2), size),
    }

# ── Measurement ──────────────────────────────────────────────────────────────

def measure(func, data: list, reps: int = 3) -> tuple[float, list]:
    best = float('inf')
    result = None
    for _ in range(reps):
        gc.disable()
        t0 = time.perf_counter()
        result = func(data)
        elapsed = time.perf_counter() - t0
        gc.enable()
        if elapsed < best:
            best = elapsed
    return best, result

def fmt_time(t: float) -> str:
    if t < 1e-6: return f"{t*1e9:.0f}ns"
    if t < 1e-3: return f"{t*1e6:.1f}µs"
    if t < 1:    return f"{t*1e3:.2f}ms"
    return f"{t:.3f}s"

def verify(result: list, reference: list) -> bool:
    return result == reference

# ── Main benchmark ───────────────────────────────────────────────────────────

def run_benchmark(
    algo_names: list[str] | None = None,
    filter_str: str | None = None,
    top_n: int | None = None,
    dataset_size: int = 100,
    reps: int = 3,
):
    datasets = make_datasets(dataset_size)
    references = {name: sorted(data) for name, data in datasets.items()}

    # select algorithms
    if algo_names:
        algos = {k: v for k, v in REGISTRY.items()
                 if any(a.lower() in k.lower() for a in algo_names)}
    elif filter_str:
        algos = {k: v for k, v in REGISTRY.items()
                 if filter_str.lower() in k.lower()}
    else:
        algos = dict(REGISTRY)

    algos = {k: v for k, v in sorted(algos.items()) if k not in SKIP_ALL}

    if not algos:
        print("No algorithms match the filter.")
        return

    # column widths
    col_w = 14
    name_w = 30
    ds_names = list(datasets.keys())

    print("=" * (name_w + col_w * len(ds_names) + 8))
    print(f"  Sorting Benchmark  •  {len(algos)} algorithms  •  size={dataset_size}  •  reps={reps}")
    print("=" * (name_w + col_w * len(ds_names) + 8))
    header = f"{'Algorithm':<{name_w}}"
    for ds in ds_names:
        header += f"{ds[:col_w-1]:>{col_w}}"
    header += f"  {'OK':>4}"
    print(header)
    print("-" * (name_w + col_w * len(ds_names) + 8))

    results_summary: list[tuple[str, float, bool, bool]] = []

    for name, func in algos.items():
        is_no_verify = name in NO_VERIFY

        # special tiny-data algorithms
        if name in SPECIAL_DATA:
            special_data, label = SPECIAL_DATA[name]
            row = f"{name:<{name_w}}"
            row += f"{'—':>{col_w}}" * (len(ds_names) - 1)
            try:
                t, res = measure(func, special_data, reps=1)
                row += f"{fmt_time(t):>{col_w}}"
            except Exception:
                t = 0.0
                row += f"{'ERR':>{col_w}}"
            tag = "~" if is_no_verify else "✓"
            print(row + f"  {tag:>4}")
            results_summary.append((name, t, True, is_no_verify))
            continue

        row = f"{name:<{name_w}}"
        total_time = 0.0
        all_correct = True

        for ds_name, data in datasets.items():
            is_large = "Large" in ds_name
            if is_large and name in SKIP_LARGE:
                row += f"{'skip':>{col_w}}"
                continue
            try:
                t, res = measure(func, data, reps=reps)
                total_time += t
                if not is_no_verify and not verify(res, references[ds_name]):
                    all_correct = False
                row += f"{fmt_time(t):>{col_w}}"
            except Exception:
                row += f"{'ERR':>{col_w}}"
                all_correct = False

        tag = "~" if is_no_verify else ("✓" if all_correct else "✗")
        print(row + f"  {tag:>4}")
        results_summary.append((name, total_time, all_correct, is_no_verify))

    print("=" * (name_w + col_w * len(ds_names) + 8))

    # ranking
    ranked = sorted(
        [(n, t) for n, t, ok, skip_v in results_summary
         if ok and not skip_v and t > 0],
        key=lambda x: x[1]
    )
    if top_n:
        ranked = ranked[:top_n]
    max_t = ranked[-1][1] if ranked else 1.0
    title = f"Ranking — fastest first" + (f" (top {top_n})" if top_n else "")
    print(f"\n{title}")
    print("─" * 60)
    for i, (n, t) in enumerate(ranked, 1):
        bar = "█" * max(1, int(t / max_t * 28))
        print(f"  {i:>3}. {n:<32} {fmt_time(t):>9}  {bar}")

    errors   = [n for n, _, ok, sv in results_summary if not ok and not sv]
    satirical = [n for n, _, _, sv in results_summary if sv]
    if errors:
        print(f"\n✗ Errors ({len(errors)}): {', '.join(errors)}")
    if satirical:
        print(f"\n~ Satirical/random (not verified): {', '.join(satirical)}")

    # alphabet coverage
    first = set(k[0].upper() for k in REGISTRY)
    missing = sorted(set("ABCDEFGHIJKLMNOPQRSTUVWXYZ") - first)
    print(f"\nAlphabet coverage: {len(first)}/26  |  Total: {len(REGISTRY)} algorithms")
    colored = " ".join(
        f"\033[92m{l}\033[0m" if l in first else f"\033[91m{l}\033[0m"
        for l in "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    )
    print("  " + colored)
    if missing:
        print(f"  Missing: {', '.join(missing)} ← open PR!")

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sorting algorithm benchmark")
    p.add_argument("-f",  "--filter",    default=None, help="filter by name substring")
    p.add_argument("-a",  "--algos",     default=None, help="comma-separated algorithm names")
    p.add_argument("-t",  "--top",       default=None, type=int, help="show top N in ranking")
    p.add_argument("-s",  "--size",      default=100,  type=int, help="dataset size (default 100)")
    p.add_argument("-r",  "--reps",      default=3,    type=int, help="repetitions per measurement")
    p.add_argument("-l",  "--list",      action="store_true",    help="list all algorithms and exit")
    args = p.parse_args()

    if args.list:
        print(f"{'Algorithm':<35} {'Function':<35}")
        print("─" * 70)
        for name, func in sorted(REGISTRY.items()):
            print(f"{name:<35} {func.__name__:<35}")
        print(f"\nTotal: {len(REGISTRY)} algorithms")
        sys.exit(0)

    algo_names = [a.strip() for a in args.algos.split(",")] if args.algos else None
    run_benchmark(
        algo_names=algo_names,
        filter_str=args.filter,
        top_n=args.top,
        dataset_size=args.size,
        reps=args.reps,
    )
