# 🔢 Sorting Algorithms Collection

> **55+ sorting algorithms.** From O(n log n) to O(∞). From production-ready to cosmic.

```
python benchmark.py          # find out which one is fastest
python visualize.py          # watch them in action
```

---

## 📁 Structure

```
Sorting/
├── data.py              # test datasets
├── benchmark.py         # auto-benchmark of all algorithms
├── visualize.py         # matplotlib animations
└── algorithms/
    ├── __init__.py      # auto-discovery (zero hardcoding!)
    └── *.py             # each algorithm in its own file
```

**Adding a new algorithm = adding one file.** Zero editing of other files.  
`benchmark.py` and `visualize.py` detect it automatically.

---

## 📊 Algorithms

### ⚡ O(n log n) Algorithms — Production-Ready

| Algorithm | Avg | Worst | Stable | Notes |
|---|---|---|---|---|
| TimSort | O(n log n) | O(n log n) | ✓ | Powers Python's `sorted()` |
| MergeSort | O(n log n) | O(n log n) | ✓ | Classic divide & conquer |
| QuickSort | O(n log n) | **O(n²)** | ✗ | Fastest in practice |
| KnuthSort | O(n log n) | O(n log n) | ✗ | 3-way, great on duplicates |
| IntroSort | O(n log n) | O(n log n) | ✗ | Powers C++ `std::sort` |
| HeapSort | O(n log n) | O(n log n) | ✗ | Guaranteed, in-place |
| ShellSort | O(n log²n) | O(n log²n) | ✗ | Surprisingly fast in practice |
| GrailSort | O(n log n) | O(n log n) | ✓ | **O(1) memory!** |
| WikiSort | O(n log n) | O(n log n) | ✓ | Block merge, O(1) memory |
| QuadSort | O(n log n) | O(n log n) | ✓ | Sorting network for blocks of 4 |
| SmoothSort | O(n log n) | O(n log n) | ✗ | Leonardo heap |
| TreeSort | O(n log n) | **O(n²)** | ✓ | BST in-order traversal |
| TournamentSort | O(n log n) | O(n log n) | ✗ | Tournament tree |
| PatienceSort | O(n log n) | O(n log n) | ✓ | Inspired by Patience card game |

### 🚀 Better than O(n log n) — Non-Comparison Sorts

| Algorithm | Complexity | Constraint |
|---|---|---|
| CountingSort | **O(n + k)** | integers only, range k |
| RadixSort | **O(nk)** | integers only |
| BucketSort | **O(n + k) avg** | uniform distribution |
| PigeonHoleSort | **O(n + k)** | integers only, range ≈ n |
| BeadSort | **O(S)** S=sum | non-negative integers, slow in practice |
| GravitySort | **O(S)** | non-negative integers |
| SpreadSort | **O(n) avg** | integers, Boost C++ |
| FlashSort | **O(n) avg** | uniform distribution |
| PostmanSort | **O(nk)** | MSD Radix |
| AmericanFlagSort | **O(nk)** | MSD, in-place |

### 🐌 O(n²) Algorithms — Classic & Educational

| Algorithm | Stable | Fun Fact |
|---|---|---|
| BubbleSort | ✓ | The most famous slow sort |
| InsertionSort | ✓ | Fastest on nearly-sorted data |
| SelectionSort | ✗ | Minimum memory writes (allegedly) |
| CocktailShakerSort | ✓ | BubbleSort in both directions |
| CombSort | ✗ | BubbleSort with gap > 1 |
| GnomeSort | ✓ | How a garden gnome would sort |
| ExchangeSort | ✗ | Everyone vs everyone |
| NaiveSort | ✗ | Restarts from scratch after each swap |
| OddEvenSort | ✓ | Designed for GPU/parallel execution |
| CycleSort | ✗ | **Optimal number of writes** |
| PancakeSort | ✗ | Only prefix reversals allowed |
| BurntPancakeSort | ✗ | PancakeSort with two-sided pancakes |
| StrandSort | ✓ | Pulls out sorted subsequences |
| UnstableSort | ✗ | Deliberately unstable (testing tool) |
| PopCornSort | ✓ | Custom BubbleSort variant |
| VinoSort | ✓ | Original, inspired by wine decanting 🍷 |
| JigsawSort | ✓ | Sorts in blocks like puzzle pieces |
| LibrarySort | ✓ | InsertionSort with gaps |
| DrunkSort | ✗ | 70% good move, 30% random |

### 💀 Deliberately Bad / Satirical Algorithms

| Algorithm | Complexity | Lore |
|---|---|---|
| **QuantumBogoSort** | **O(1)†** | Destroys n!-1 universes. The fastest. |
| BogoSort | O(n · n!) | Shuffle until sorted |
| BogoBogoSort | O((n+1)!) | **Do not use for n > 4. Seriously.** |
| StalinSort | O(n) | Removes elements that don't fit the order |
| SlowSort | O(n^(log n/log log n)) | Deliberately the slowest correct sort |
| StoogeSort | O(n^2.7) | "Multiply and surrender" |
| MiracleSort | O(∞) | Waits for cosmic radiation |
| SleepSort | O(max(n)) | Threads sleep for the value of each element |
| ChatGPTSort_v1 | O(n log n) + 10% errors | Hallucinations, content policy, context window |
| ChatGPTSort_v2 | O(💸/token) | Real OpenAI API |
| ClaudeSort | O(n log n) + questions | Asks for context, suggests alternatives |

> **†** Time complexity in the surviving universe: O(1).  
> Ethical complexity: O(n! × ∞) destroyed timelines.  
> Use responsibly.

### 📊 Alphabet Coverage

Every letter of the alphabet has at least one algorithm:

```
A B C D E F G H I J K L M N O P Q R S T U V W X Y Z
✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ✓ ? ? ?
```

> X, Y, Z are the legendary challenge — first person to add all three wins. (nothing except eternal glory in the commit history cause I'm broke)

---

## 🚀 Usage

```python
# import a specific algorithm
from algorithms import merge_sort, quick_sort, tim_sort

data = [64, 34, 25, 12, 22, 11, 90]
print(merge_sort(data))   # [11, 12, 22, 25, 34, 64, 90]

# import all (auto-discovery)
from algorithms import REGISTRY
for name, func in REGISTRY.items():
    print(f"{name}: {func(data)}")
```

```bash
# benchmark with filter
python benchmark.py
python benchmark.py --filter Quick

# visualization
python visualize.py
python visualize.py "Quick Sort" --size 30 --speed 20
python visualize.py --compare       # all side by side
```

---

## ➕ Adding Your Own Algorithms

### New sorting algorithm

1. Create `algorithms/XxxSort.py`
2. Implement `xxx_sort(list)` returning a **new sorted list** (don't modify in-place)
3. Done — `benchmark.py` and `__init__.py` will detect it automatically

```python
# algorithms/XyzSort.py
from data import *

def xyz_sort(lst):
    arr = lst.copy()
    # your implementation...
    return arr

if __name__ == "__main__":
    from data import random_data
    print(xyz_sort(random_data))
```

### New animation for visualize.py

```python
# in visualize.py or your own file
from visualize import register_algorithm

def _xyz_generator(lst):
    # yield (list_state, [compared_indices], [sorted_indices], "label")
    a = lst[:]
    # ... your steps ...
    yield a[:], [0, 1], [], "Comparing"
    yield a[:], [], list(range(len(a))), "Done!"

register_algorithm("XYZ Sort", _xyz_generator)
```

---

## 🤝 Pull Requests — Join the project!

**Looking for algorithms starting with: X, Y, Z** (and anything interesting)

PR rules are simple:

- **One file = one algorithm** (e.g. `XorSort.py`)  
- Sorting function must return a **new list** (`arr = lst.copy()` at the start)  
- One comment at the top: complexity + short description of how it works  
- Must pass: `assert xyz_sort([3,1,2]) == [1,2,3]`  
- Satirical/joke algorithms are welcome too (see: `StalinSort.py`, `QuantumBogoSort.py`)

**Especially wanted:**
- 🔤 **XorSort, YahooSort, ZigZagSort** — complete the alphabet!
- 🌐 **LocaleSort** — sorting with locale/collation awareness
- 🧬 **GeneticSort** — evolutionary algorithm
- 🐜 **AntSort** — ant colony algorithm (ACO)
- 🧪 **ProbabilisticSort** — probabilistic sorting
- 📐 **GeometricSort** — sorting through geometry

Every algorithm you add lives here alongside QuantumBogoSort. That's an honor.

---

## 📈 Complexity & Fun Facts

```
Fastest (theory):       QuantumBogoSort — O(1) in the surviving universe
Fastest (practice):     SpreadSort / CountingSort — O(n)
Slowest (correct):      SlowSort — O(n^(log n / log log n))
Slowest (overall):      MiracleSort — O(∞)
Fewest writes:          CycleSort — minimal number of write operations
Most stable:            TimSort — used in CPython and Java
Most dramatic:          QuantumBogoSort — destroys universes
Most honest:            StalinSort — always O(n), always "sorted"
```

---

*"Every sorting algorithm is correct if you define 'sorted' appropriately."*  
*— StalinSort Documentation, 2024*