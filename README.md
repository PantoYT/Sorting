# 🔢 Sorting Algorithms Collection

> **100 sorting algorithms.** From O(1) to O(∞). From production-ready to multiverse-borrowing.

```bash
python benchmark.py                         # full benchmark
python benchmark.py -a BubbleSort,TimSort   # specific algorithms
python benchmark.py -f Quick --top 5        # filter + top 5
python benchmark.py --list                  # list all 100

python visualize.py                         # interactive menu
python visualize.py QuickSort               # single animation
python visualize.py Bubble,Merge,Quick      # compare side-by-side
python visualize.py --list                  # list visualizable algorithms
```

---

## 📁 Structure

```
Sorting/
├── data.py              # test datasets
├── benchmark.py         # auto-benchmark, zero hardcoding
├── visualize.py         # matplotlib animations, comma-list compare
└── algorithms/
    ├── __init__.py      # auto-discovery
    └── *.py             # 100 algorithms, one per file
```

**Adding a new algorithm = one new file.** Everything else updates automatically.

---

## 📊 All 100 Algorithms

### ⚡ O(n log n) — Production Ready

| Algorithm | Avg | Worst | Stable | Notes |
|---|---|---|---|---|
| TimSort | O(n log n) | O(n log n) | ✓ | Powers Python `sorted()` |
| MergeSort | O(n log n) | O(n log n) | ✓ | Classic divide & conquer |
| IterativeMergeSort | O(n log n) | O(n log n) | ✓ | No recursion, stack-safe |
| AdaptiveMergeSort | O(n log k) | O(n log n) | ✓ | k = number of runs |
| WeaveMergeSort | O(n log n) | O(n log n) | ✓ | Cache-friendly bottom-up |
| InPlaceMergeSort | O(n log²n) | O(n log²n) | ✓ | O(1) extra memory |
| MergeSortParallel | O(n log n) | O(n log n) | ✓ | Multi-threaded |
| QuickSort | O(n log n) | **O(n²)** | ✗ | Fastest in practice |
| RandomizedQuickSort | O(n log n) | **O(n²)** rare | ✗ | Random pivot |
| StableQuickSort | O(n log n) | **O(n²)** | ✓ | Extra memory for stability |
| TernarySplitQuickSort | O(n log n) | O(n log n) | ✗ | Dutch flag partition |
| DualPivotQuickSort | O(n log n) | O(n log n) | ✗ | Java `Arrays.sort()` |
| KnuthSort | O(n log n) | O(n log n) | ✗ | 3-way, Knuth vol.3 |
| IntroSort | O(n log n) | O(n log n) | ✗ | C++ `std::sort` |
| HeapSort | O(n log n) | O(n log n) | ✗ | Guaranteed, in-place |
| SmoothSort | O(n log n) | O(n log n) | ✗ | Leonardo heap |
| ShellSort | O(n log²n) | O(n log²n) | ✗ | Surprisingly fast |
| GrailSort | O(n log n) | O(n log n) | ✓ | O(1) memory |
| WikiSort | O(n log n) | O(n log n) | ✓ | Block merge, O(1) memory |
| QuadSort | O(n log n) | O(n log n) | ✓ | Sorting network for 4-blocks |
| BitonicSort | O(n log²n) | O(n log²n) | ✗ | GPU-friendly |
| BitonicMergeSort | O(n log²n) | O(n log²n) | ✗ | Explicit merge network |
| SortingNetwork | O(n log²n) | O(n log²n) | ✗ | Fixed comparator network |
| TreeSort | O(n log n) | **O(n²)** | ✓ | BST in-order |
| TournamentSort | O(n log n) | O(n log n) | ✗ | Tournament tree |
| PatienceSort | O(n log n) | O(n log n) | ✓ | Patience solitaire |
| PatienceOptSort | O(n log n) | O(n log n) | ✓ | Binary search piles |
| PatienceSortIterative | O(n log n) | O(n log n) | ✓ | No recursion |
| PatienceMergeSort | O(n log n) | O(n log n) | ✓ | Patience + k-way merge |
| DropMergeSort | O(n log n) | O(n log n) | ✓ | O(n) on nearly sorted |
| StrandSort | O(n²) worst | O(n) best | ✓ | Extracts sorted runs |
| WeaveSort | O(n log n) | O(n log n) | ✓ | Bottom-up weaving |
| CartesianSort | O(n log n) | **O(n²)** | ✗ | Cartesian tree |
| FunnelSort | O(n log²n) | O(n log²n) | ✓ | Cache-oblivious |
| SampleSort | O(n log n) | O(n log n) | ✓ | Parallel-friendly |
| HybridSort | O(n log n) | O(n log n) | ✓ | Adaptive: picks best algo |
| BlockSort | O(n log n) | O(n log n) | ✓ | sqrt(n) blocks |
| LazySort | O(n log n) | O(n log n) | ✓ | Defers sort until access |
| YogurtSort | O(n log n) | O(n log n) | ✓ | Natural runs + merge |

### 🚀 Faster than O(n log n) — Non-Comparison

| Algorithm | Complexity | Constraint |
|---|---|---|
| CountingSort | **O(n + k)** | integers, range k |
| RadixSort | **O(nk)** | integers |
| BucketSort | **O(n + k) avg** | uniform distribution |
| PigeonHoleSort | **O(n + k)** | integers, range ≈ n |
| PigeonSort | **O(n + k)** | integers, pigeonhole variant |
| PigeonRaceSort | **O(n + k)** | satirical pigeonhole |
| BeadSort | **O(S)** | non-negative integers |
| GravitySort | **O(S)** | non-negative integers |
| SpreadSort | **O(n) avg** | Boost C++ |
| FlashSort | **O(n) avg** | uniform distribution |
| PostmanSort | **O(nk)** | MSD Radix |
| AmericanFlagSort | **O(nk)** | MSD, in-place |
| ProxmapSort | **O(n) avg** | uniform distribution |

### 🐌 O(n²) — Classic & Educational

| Algorithm | Stable | Notes |
|---|---|---|
| BubbleSort | ✓ | The famous one |
| ReverseBubbleSort | ✓ | Scans right-to-left |
| AntiBubbleSort | ✗ | Reverses correctly ordered pairs |
| InsertionSort | ✓ | Best on nearly-sorted |
| BinaryInsertionSort | ✓ | Binary search for position |
| RecursiveInsertionSort | ✓ | Recursive variant |
| SelectionSort | ✗ | Fewest writes |
| ExchangeSort | ✗ | Every element vs every other |
| CocktailShakerSort | ✓ | Bidirectional bubble |
| CombSort | ✗ | Bubble with gap > 1 |
| GnomeSort | ✓ | Garden gnome algorithm |
| NaiveSort | ✗ | Restarts after every swap |
| OddEvenSort | ✓ | GPU/parallel design |
| EvenOddTranspositionSort | ✓ | SIMD variant |
| CycleSort | ✗ | Minimal writes |
| PancakeSort | ✗ | Prefix reversals only |
| BurntPancakeSort | ✗ | Two-sided pancakes |
| PancakeNumberSort | ✗ | Tracks flip sequence |
| PancakeSortOptimized | ✗ | 2*(n-1) flips max |
| LibrarySort | ✓ | Insertion with gaps |
| ShuffleSort | ✗ | Fisher-Yates shuffle attempt |
| EfficientBogoSort | ✗ | "Optimized" BogoSort |
| UnstableSort | ✗ | Deliberately unstable |
| XorSort | ✗ | XOR swap trick |
| ZigZagSort | ✓ | Zigzag weave |

### 🌿 Nature-Inspired

| Algorithm | Notes |
|---|---|
| GeneticSort | Evolutionary, crossover + mutation |
| AntSort | Ant colony optimization |
| QuantumSort | Simulates quantum parallelism |
| VinoSort | Wine decanting metaphor 🍷 |
| YogurtSort | Fermentation/culture merging |
| JigsawSort | Puzzle-piece block fitting |

### 💀 Satirical / Deliberately Bad

| Algorithm | Complexity | Lore |
|---|---|---|
| **QuantumBogoSort** | **O(1)†** | Borrows result from a sorted parallel universe |
| BogoSort | O(n · n!) | Random shuffle until sorted |
| BogoBogoSort | O((n+1)!) | **n > 4 will outlive the sun** |
| StalinSort | O(n) | Removes non-conforming elements |
| SlowSort | O(n^(log n/log log n)) | Deliberately slowest correct sort |
| StoogeSort | O(n^2.7) | "Multiply and surrender" |
| MiracleSort | O(∞) | Awaits cosmic radiation |
| SleepSort | O(max(n)) | Thread sleep = element value |
| GaslitSort | O(1) (claimed) | Denies having sorted anything |
| McCarthySort | O(n! · n) | Removes random elements recursively |
| CorruptionSort | O(n log n) + bugs | Sorts then corrupts 8% |
| AntiBubbleSort | O(n²) | Unsorting machine |
| EscapeSort | O(n²) | Elements try to escape position |
| OscarSort | O(n²) | Complains the entire time |
| DrunkSort | O(?) | 70% correct, 30% chaos |
| ChatGPTSort_v1 | O(n log n) + 10% hallucinations | Context window, content policy |
| ChatGPTSort_v2 | O(💸/token) | Real OpenAI API |
| ClaudeSort | O(n log n) + questions | Asks for context first |

> **†** Time complexity: O(1) — just an observation.
> The sorted universe already exists. We just needed to look.

### 📊 Alphabet Coverage

Every letter A–Z has at least one algorithm:

```
A  B  C  D  E  F  G  H  I  J  K  L  M
✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓

N  O  P  Q  R  S  T  U  V  W  X  Y  Z
✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓  ✓
```

All 26/26 covered. 🎉

---

## 🚀 Usage

```python
from algorithms import merge_sort, quick_sort, tim_sort, REGISTRY

data = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(data))   # [11, 12, 22, 25, 34, 64, 90]

# iterate all algorithms
for name, func in REGISTRY.items():
    result = func(data[:])
```

```bash
# Benchmark examples
python benchmark.py                          # all 100
python benchmark.py -a "Merge,Quick,Tim"     # compare three
python benchmark.py -f Pancake --size 50     # filter + custom size
python benchmark.py --list                   # full list

# Visualizer examples
python visualize.py                          # menu
python visualize.py QuickSort --size 30      # single, 30 elements
python visualize.py Bubble,Merge,Quick       # compare 3 side-by-side
python visualize.py --list                   # list visualizable
```

---

## ➕ Adding Your Own Algorithm

1. Create `algorithms/XxxSort.py`
2. Implement `xxx_sort(list)` — must **return a new list**, not modify in-place
3. Done. `benchmark.py`, `__init__.py` detect it automatically.

```python
# algorithms/XyzSort.py
from data import *

def xyz_sort(lista):
    lst = lista.copy()
    # your implementation
    return lst

if __name__ == "__main__":
    from data import losowa
    print(xyz_sort(losowa))
```

### Add a visualization

```python
# in your own file or directly in visualize.py
from visualize import register_algorithm

def _xyz_steps(lst):
    a = lst[:]
    # yield (state, compare_indices, sorted_indices, label)
    yield a[:], [0, 1], [], "Comparing"
    yield a[:], [], list(range(len(a))), "Done!"

register_algorithm("XYZ Sort", _xyz_steps)
```

---

## 🤝 Pull Requests

Simple rules:
- **One file = one algorithm** (`XxxSort.py`)
- Return a **new list** (`lst = lista.copy()` at the start)
- Top comment: complexity + how it works
- Must pass: `assert xxx_sort([3,1,2]) == [1,2,3]`
- Satirical algorithms welcome (see `QuantumBogoSort.py`, `GaslitSort.py`)

**Ideas:**
- 🧬 More evolutionary algorithms (Particle Swarm, Simulated Annealing)
- 🌐 LocaleSort — locale-aware string sorting
- 🔢 More radix variants (MSD, ternary)
- 🎮 Any algorithm with a good story

Every algorithm you add lives here alongside QuantumBogoSort. That's an honor.

---

## 📈 Fun Facts

```
Fastest (theory):    QuantumBogoSort  — O(1) in the surviving universe
Fastest (practice):  SpreadSort       — O(n) average
Slowest (correct):   SlowSort         — O(n^(log n / log log n))
Slowest (overall):   MiracleSort      — O(∞)
Most honest:         StalinSort       — always O(n), always "sorted"
Most philosophical:  QuantumBogoSort  — the sorted list already exists, somewhere
Most paranoid:       GaslitSort       — denies everything
Most Java:           DualPivotQuick   — literally what Java uses
Most Python:         TimSort          — literally what Python uses
Most pigeon:         PigeonRaceSort   — n pigeons, simultaneously airborne
```

---

*"Every sorting algorithm is correct if you define 'sorted' appropriately."*  
*— StalinSort Documentation, 2024*
