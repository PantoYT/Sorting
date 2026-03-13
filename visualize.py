"""
Sorting Algorithm Visualizer

Usage:
    python visualize.py                            # interactive menu, pick by number
    python visualize.py 1                          # single algorithm by number
    python visualize.py 1,3,7                      # compare by numbers
    python visualize.py "Quick Sort"               # single by name
    python visualize.py "Bubble,Merge,Quick"       # compare by name
    python visualize.py --size 30 --speed 25
    python visualize.py --list
"""
import sys, os, random, argparse
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

try:
    import matplotlib
    matplotlib.use("TkAgg" if os.name == "nt" else "Agg")
    import matplotlib.pyplot as plt
    import matplotlib.animation as animation
    import matplotlib.gridspec as gridspec
except ImportError:
    print("Missing matplotlib: pip install matplotlib")
    sys.exit(1)

# ── Colors ────────────────────────────────────────────────────────────────────
BG    = "#1E1E2E"
C_DEF = "#4C9BE8"
C_CMP = "#FF6B6B"
C_SRT = "#6BCB77"
C_PIV = "#FFD93D"

# ── Step generators ───────────────────────────────────────────────────────────
# Each yields: (state, compare_indices, sorted_indices, label)

def _bubble(lst):
    n = len(lst); a = lst[:]
    for i in range(n - 1):
        for j in range(n - i - 1):
            yield a[:], [j, j+1], list(range(n-i, n)), f"Compare {a[j]} vs {a[j+1]}"
            if a[j] > a[j+1]:
                a[j], a[j+1] = a[j+1], a[j]
                yield a[:], [j, j+1], list(range(n-i, n)), "Swap"
    yield a[:], [], list(range(n)), "Done"

def _selection(lst):
    n = len(lst); a = lst[:]
    for i in range(n):
        m = i
        for j in range(i+1, n):
            yield a[:], [m, j], list(range(i)), f"Min={a[m]}, check {a[j]}"
            if a[j] < a[m]: m = j
        a[i], a[m] = a[m], a[i]
        yield a[:], [i], list(range(i+1)), f"Place {a[i]} at {i}"
    yield a[:], [], list(range(n)), "Done"

def _insertion(lst):
    n = len(lst); a = lst[:]
    for i in range(1, n):
        key = a[i]; j = i - 1
        yield a[:], [i], list(range(i)), f"Insert key={key}"
        while j >= 0 and a[j] > key:
            yield a[:], [j, j+1], list(range(i)), f"Shift {a[j]} right"
            a[j+1] = a[j]; j -= 1
        a[j+1] = key
        yield a[:], [j+1], list(range(i+1)), f"Placed {key}"
    yield a[:], [], list(range(n)), "Done"

def _merge(lst):
    steps = []; a = lst[:]
    def ms(l, r):
        if r - l <= 1: return
        m = (l + r) // 2
        ms(l, m); ms(m, r)
        left, right = a[l:m], a[m:r]
        i = j = 0; k = l
        while i < len(left) and j < len(right):
            steps.append((a[:], [l+i, m+j], [], f"Merge: {left[i]} vs {right[j]}"))
            if left[i] <= right[j]: a[k]=left[i]; i+=1
            else: a[k]=right[j]; j+=1
            k+=1
        while i<len(left): a[k]=left[i]; i+=1; k+=1
        while j<len(right): a[k]=right[j]; j+=1; k+=1
        steps.append((a[:], list(range(l,r)), [], f"Merged [{l}:{r}]"))
    ms(0, len(a))
    for s in steps: yield s
    yield a[:], [], list(range(len(a))), "Done"

def _quick(lst):
    steps = []; a = lst[:]
    def qs(lo, hi):
        if lo >= hi: return
        pivot = a[hi]
        steps.append((a[:], [hi], [], f"Pivot={pivot}"))
        i = lo - 1
        for j in range(lo, hi):
            steps.append((a[:], [j, hi], [], f"{a[j]} vs pivot {pivot}"))
            if a[j] <= pivot:
                i += 1; a[i], a[j] = a[j], a[i]
                if i!=j: steps.append((a[:], [i,j], [], "Swap"))
        a[i+1], a[hi] = a[hi], a[i+1]
        steps.append((a[:], [i+1], [], f"Pivot {pivot} at {i+1}"))
        qs(lo, i); qs(i+2, hi)
    qs(0, len(a)-1)
    for s in steps: yield s
    yield a[:], [], list(range(len(a))), "Done"

def _heap(lst):
    steps = []; a = lst[:]
    def hfy(n, i):
        lg=i; l=2*i+1; r=2*i+2
        if l<n and a[l]>a[lg]: lg=l
        if r<n and a[r]>a[lg]: lg=r
        if lg!=i:
            steps.append((a[:],[i,lg],[],"Heapify"))
            a[i],a[lg]=a[lg],a[i]; hfy(n,lg)
    n=len(a)
    for i in range(n//2-1,-1,-1): hfy(n,i)
    for i in range(n-1,0,-1):
        a[0],a[i]=a[i],a[0]
        steps.append((a[:],[0,i],list(range(i,n)),f"Extract max→{i}"))
        hfy(i,0)
    for s in steps: yield s
    yield a[:], [], list(range(n)), "Done"

def _shell(lst):
    a=lst[:]; n=len(a); gap=n//2
    while gap>0:
        for i in range(gap,n):
            temp=a[i]; j=i
            yield a[:],[j],[]  ,f"Gap={gap}"
            while j>=gap and a[j-gap]>temp:
                a[j]=a[j-gap]; j-=gap
                yield a[:],[j],[],"Shift"
            a[j]=temp
        gap//=2
    yield a[:],[],list(range(n)),"Done"

def _counting(lst):
    a=lst[:]; n=len(a); mn,mx=min(a),max(a)
    cnt=[0]*(mx-mn+1)
    for x in a:
        cnt[x-mn]+=1
        yield a[:],[],[],f"Count {x}"
    result=[]
    for i,c in enumerate(cnt):
        result.extend([i+mn]*c)
        if c: yield result+a[len(result):],list(range(len(result)-c,len(result))),[]  ,f"Output {i+mn}×{c}"
    yield result,[],list(range(n)),"Done"

def _radix(lst):
    a=lst[:]; steps=[]
    def cpass(arr,exp):
        n=len(arr); out=[0]*n; cnt=[0]*10
        for x in arr: cnt[(x//exp)%10]+=1
        for i in range(1,10): cnt[i]+=cnt[i-1]
        for i in range(n-1,-1,-1):
            idx=(arr[i]//exp)%10; out[cnt[idx]-1]=arr[i]; cnt[idx]-=1
            steps.append((arr[:],[i],[]  ,f"exp={exp} digit {idx}"))
        return out
    exp=1
    while max(a)//exp>0:
        a=cpass(a,exp)
        steps.append((a[:],[],list(range(len(a))),f"Pass exp={exp}"))
        exp*=10
    for s in steps: yield s
    yield a,[],list(range(len(a))),"Done"

def _gnome(lst):
    a=lst[:]; n=len(a); i=0
    while i<n:
        if i==0 or a[i]>=a[i-1]:
            yield a[:],[i],[],f"Step → {i+1}"; i+=1
        else:
            yield a[:],[i,i-1],[],"Swap back"
            a[i],a[i-1]=a[i-1],a[i]; i-=1
    yield a[:],[],list(range(n)),"Done"

def _cocktail(lst):
    a=lst[:]; n=len(a); s,e=0,n-1
    while s<e:
        sw=False
        for i in range(s,e):
            yield a[:],[i,i+1],[],"→"
            if a[i]>a[i+1]: a[i],a[i+1]=a[i+1],a[i]; sw=True
        e-=1
        for i in range(e,s,-1):
            yield a[:],[i,i-1],[],"←"
            if a[i]<a[i-1]: a[i],a[i-1]=a[i-1],a[i]; sw=True
        s+=1
        if not sw: break
    yield a[:],[],list(range(n)),"Done"

def _comb(lst):
    a=lst[:]; n=len(a); gap=n; sw=True
    while gap>1 or sw:
        gap=max(1,int(gap/1.3)); sw=False
        for i in range(n-gap):
            yield a[:],[i,i+gap],[],f"Gap={gap}"
            if a[i]>a[i+gap]: a[i],a[i+gap]=a[i+gap],a[i]; sw=True
    yield a[:],[],list(range(n)),"Done"

def _bitonic(lst):
    import math
    a=lst[:]; n=len(a)
    sz=2**math.ceil(math.log2(n)) if n>1 else 1
    a+=[float('inf')]*(sz-n); steps=[]
    def cs(i,j,d):
        if (a[i]>a[j])==d: a[i],a[j]=a[j],a[i]; steps.append((a[:n],[i,j],[],"Swap"))
        else: steps.append((a[:n],[i,j],[],"Keep"))
    def bm(lo,cnt,d):
        if cnt>1:
            k=cnt//2
            for i in range(lo,lo+k): cs(i,i+k,d)
            bm(lo,k,d); bm(lo+k,k,d)
    def bs(lo,cnt,d):
        if cnt>1:
            k=cnt//2; bs(lo,k,True); bs(lo+k,k,False); bm(lo,cnt,d)
    bs(0,sz,True)
    for s in steps: yield s
    yield a[:n],[],list(range(n)),"Done"

def _strand(lst):
    a=lst[:]; result=[]
    while a:
        strand=[a.pop(0)]; rem=[]
        for x in a:
            if x>=strand[-1]: strand.append(x)
            else: rem.append(x)
        a=rem
        merged=[]; i=j=0
        while i<len(result) and j<len(strand):
            if result[i]<=strand[j]: merged.append(result[i]); i+=1
            else: merged.append(strand[j]); j+=1
        merged.extend(result[i:]); merged.extend(strand[j:])
        result=merged
        yield result+[0]*(len(lst)-len(result)),[],[],f"Strand len={len(strand)}"
    yield result,[],list(range(len(lst))),"Done"

def _odd_even(lst):
    a=lst[:]; n=len(a); done=False
    while not done:
        done=True
        for i in range(0,n-1,2):
            yield a[:],[i,i+1],[],"Even"
            if a[i]>a[i+1]: a[i],a[i+1]=a[i+1],a[i]; done=False
        for i in range(1,n-1,2):
            yield a[:],[i,i+1],[],"Odd"
            if a[i]>a[i+1]: a[i],a[i+1]=a[i+1],a[i]; done=False
    yield a[:],[],list(range(n)),"Done"

def _pancake(lst):
    a=lst[:]; n=len(a)
    def flip(k): a[:k+1]=a[:k+1][::-1]
    for size in range(n,1,-1):
        mi=a.index(max(a[:size]))
        if mi!=size-1:
            if mi!=0: yield a[:],[mi],[],"Find max"; flip(mi)
            yield a[:],[0,size-1],[],"Flip to position"; flip(size-1)
            yield a[:],[size-1],list(range(size,n)),f"Max at {size-1}"
    yield a[:],[],list(range(n)),"Done"

def _stalin(lst):
    a=lst[:]; result=[a[0]]
    for x in a[1:]:
        yield a[:],[a.index(x) if x in a else 0],[],f"Evaluate {x}"
        if x>=result[-1]: result.append(x)
        else: yield result+a[len(result):],[len(result)-1],[]  ,f"ELIMINATED: {x}"
    yield result,[],list(range(len(result))),"Purged"

def _patience(lst):
    import heapq, bisect
    a=lst[:]; piles=[]; tops=[]; ss=[]
    for x in a:
        pos=bisect.bisect_left(tops,x)
        if pos<len(piles): piles[pos].append(x); tops[pos]=x
        else: piles.append([x]); tops.append(x)
        flat=[v for p in piles for v in p]
        ss.append((flat[:]+[0]*(len(a)-len(flat)),[len(flat)-1],[],f"→ pile {pos+1}/{len(piles)}"))
    for s in ss: yield s
    heap=[]
    for i,p in enumerate(piles): heapq.heappush(heap,(p.pop(),i))
    result=[]
    while heap:
        val,i=heapq.heappop(heap)
        result.append(val)
        yield result+[0]*(len(a)-len(result)),[len(result)-1],list(range(len(result)-1)),f"Extracted {val}"
        if piles[i]: heapq.heappush(heap,(piles[i].pop(),i))
    yield result,[],list(range(len(a))),"Done"

def _exchange(lst):
    a=lst[:]; n=len(a)
    for i in range(n-1):
        for j in range(i+1,n):
            yield a[:],[i,j],list(range(i)),f"{a[i]} vs {a[j]}"
            if a[i]>a[j]: a[i],a[j]=a[j],a[i]
    yield a[:],[],list(range(n)),"Done"

def _cycle(lst):
    a=lst[:]; n=len(a); steps=[]
    for cs in range(n-1):
        item=a[cs]; pos=cs
        for i in range(cs+1,n):
            if a[i]<item: pos+=1
        if pos==cs: continue
        while item==a[pos]: pos+=1
        a[pos],item=item,a[pos]; steps.append((a[:],[pos,cs],[],"Cycle place"))
        while pos!=cs:
            pos=cs
            for i in range(cs+1,n):
                if a[i]<item: pos+=1
            while item==a[pos]: pos+=1
            a[pos],item=item,a[pos]; steps.append((a[:],[pos],[],"Cycle cont."))
    for s in steps: yield s
    yield a[:],[],list(range(n)),"Done"

def _knuth(lst):
    steps=[]; a=lst[:]
    def s3(lo,hi):
        if hi<=lo: return
        lt,gt=lo,hi; piv=a[lo]; i=lo+1
        steps.append((a[:],[lo],[],f"3-way pivot={piv}"))
        while i<=gt:
            if a[i]<piv: a[lt],a[i]=a[i],a[lt]; lt+=1; i+=1
            elif a[i]>piv: a[i],a[gt]=a[gt],a[i]; gt-=1
            else: i+=1
        s3(lo,lt-1); s3(gt+1,hi)
    s3(0,len(a)-1)
    for s in steps: yield s
    yield a[:],[],list(range(len(a))),"Done"

# ── Visual Registry ───────────────────────────────────────────────────────────

VISUAL_REGISTRY: dict[str, callable] = {
    "Bubble Sort":         _bubble,
    "Selection Sort":      _selection,
    "Insertion Sort":      _insertion,
    "Merge Sort":          _merge,
    "Quick Sort":          _quick,
    "Heap Sort":           _heap,
    "Shell Sort":          _shell,
    "Counting Sort":       _counting,
    "Radix Sort":          _radix,
    "Gnome Sort":          _gnome,
    "Cocktail Sort":       _cocktail,
    "Comb Sort":           _comb,
    "Bitonic Sort":        _bitonic,
    "Strand Sort":         _strand,
    "Odd-Even Sort":       _odd_even,
    "Pancake Sort":        _pancake,
    "Stalin Sort":         _stalin,
    "Patience Sort":       _patience,
    "Exchange Sort":       _exchange,
    "Cycle Sort":          _cycle,
    "Knuth 3-way":         _knuth,
}

ALGO_LIST = list(VISUAL_REGISTRY.keys())  # numbered 1..N

def register_algorithm(name: str, gen_func: callable):
    VISUAL_REGISTRY[name] = gen_func
    if name not in ALGO_LIST:
        ALGO_LIST.append(name)

# ── Rendering ─────────────────────────────────────────────────────────────────

def _style(ax):
    ax.set_facecolor(BG)
    for sp in ax.spines.values():
        sp.set_edgecolor("#333")
    ax.tick_params(colors="#555", labelsize=7)

def _animate(fig, axes_bars, all_steps, interval):
    max_frames = max(len(s) for s in all_steps)

    def update(frame):
        for (ax, bars), steps in zip(axes_bars, all_steps):
            f = min(frame, len(steps) - 1)
            state, cmp, srt, _ = steps[f]
            for i, bar in enumerate(bars):
                bar.set_color(C_SRT if i in srt else C_CMP if i in cmp else C_DEF)
                bar.set_height(state[i] if i < len(state) else 0)
        return [b for _, bars in axes_bars for b in bars]

    ani = animation.FuncAnimation(fig, update, frames=max_frames,
                                  interval=interval, blit=False, repeat=False)
    plt.tight_layout()
    plt.show()
    plt.close()

def visualize_single(name: str, data: list, interval: int = 40):
    steps = list(VISUAL_REGISTRY[name](data[:]))
    n = len(data)

    fig = plt.figure(figsize=(12, 5), facecolor=BG)
    gs  = gridspec.GridSpec(1, 2, width_ratios=[4, 1], wspace=0.04)
    ax  = fig.add_subplot(gs[0])
    axr = fig.add_subplot(gs[1])
    _style(ax); axr.set_facecolor(BG); axr.axis("off")

    ax.set_title(name, color="white", fontsize=13, fontweight="bold", pad=8)
    bars = ax.bar(range(n), steps[0][0], color=C_DEF, edgecolor=BG, linewidth=0.4)
    ax.set_xlim(-0.5, n - 0.5)
    ax.set_ylim(0, max(data) * 1.12)

    info = axr.text(0.05, 0.92, "", transform=axr.transAxes, color="white",
                    fontsize=8, va="top", family="monospace",
                    bbox=dict(boxstyle="round,pad=0.5", facecolor="#2a2a3e", edgecolor="#555"))

    def update(frame):
        if frame >= len(steps): return bars,
        state, cmp, srt, label = steps[frame]
        for i, bar in enumerate(bars):
            bar.set_color(C_SRT if i in srt else C_CMP if i in cmp else C_DEF)
            bar.set_height(state[i] if i < len(state) else 0)
        pct = (frame + 1) / len(steps) * 100
        info.set_text(f"Step {frame+1}/{len(steps)}\n{pct:.0f}%\n\n{label[:28]}\n\nn={n}")
        return bars,

    ani = animation.FuncAnimation(fig, update, frames=len(steps),
                                  interval=interval, blit=False, repeat=False)
    plt.tight_layout(); plt.show(); plt.close()

def visualize_compare(names: list[str], data: list, interval: int = 40):
    k = len(names)
    n = len(data)
    all_steps = [list(VISUAL_REGISTRY[name](data[:])) for name in names]

    cols = min(k, 3)
    rows = (k + cols - 1) // cols
    fig, axes = plt.subplots(rows, cols, figsize=(5*cols, 4*rows), facecolor=BG)
    if k == 1: axes = [[axes]]
    elif rows == 1: axes = [axes]
    flat = [ax for row in axes for ax in row]

    axes_bars = []
    for idx, (name, steps) in enumerate(zip(names, all_steps)):
        ax = flat[idx]; _style(ax)
        ax.set_title(name, color="white", fontsize=9, pad=4, fontweight="bold")
        bars = ax.bar(range(n), steps[0][0], color=C_DEF, edgecolor=BG, linewidth=0.3)
        ax.set_xlim(-0.5, n-0.5); ax.set_ylim(0, max(data)*1.1)
        axes_bars.append((ax, bars))

    for idx in range(k, len(flat)): flat[idx].set_visible(False)
    fig.suptitle(f"Comparing {k} algorithms  (n={n})", color="white", fontsize=11)
    _animate(fig, axes_bars, all_steps, interval)

# ── Menu ──────────────────────────────────────────────────────────────────────

def _print_list():
    print("\n╔══════════════════════════════════════════════════════════╗")
    print("║          SORTING ALGORITHM VISUALIZER                   ║")
    print("╚══════════════════════════════════════════════════════════╝\n")
    cols = 2
    n = len(ALGO_LIST)
    half = (n + 1) // 2
    for i in range(half):
        left  = f"{i+1:>3}. {ALGO_LIST[i]}"
        right = f"{i+half+1:>3}. {ALGO_LIST[i+half]}" if i+half < n else ""
        print(f"  {left:<32}  {right}")
    print()

def _resolve(tokens: list[str]) -> list[str]:
    """Resolve a list of tokens (numbers or name fragments) to algorithm names."""
    selected = []
    for tok in tokens:
        tok = tok.strip()
        if not tok:
            continue
        if tok.isdigit():
            idx = int(tok) - 1
            if 0 <= idx < len(ALGO_LIST):
                selected.append(ALGO_LIST[idx])
            else:
                print(f"  No algorithm #{tok}")
        else:
            q = tok.lower().replace(" ", "")
            matches = [name for name in ALGO_LIST
                       if q in name.lower().replace(" ", "")]
            if matches:
                selected.append(matches[0])
            else:
                print(f"  No match for '{tok}'")
    return list(dict.fromkeys(selected))

def menu():
    sizes = [10, 20, 30, 50]

    _print_list()
    print("Enter algorithm numbers or names, comma-separated.")
    print("Examples:  1          → animate #1")
    print("           1,3,7      → compare #1 #3 #7")
    print("           Quick,Heap → compare by name")
    print()

    try:
        raw   = input("Algorithm(s): ").strip()
        s_in  = input(f"Size [1={sizes[0]}, 2={sizes[1]}, 3={sizes[2]}, 4={sizes[3]}] (Enter=2): ").strip() or "2"
        sp_in = input("Speed ms/step (Enter=40): ").strip() or "40"
    except (KeyboardInterrupt, EOFError):
        return

    if not raw or raw == "0":
        return

    size     = sizes[min(3, max(0, int(s_in) - 1))]
    interval = max(10, int(sp_in))
    data     = random.sample(range(1, size + 1), size)
    tokens   = [t.strip() for t in raw.split(",")]
    selected = _resolve(tokens)

    if not selected:
        print("Nothing to visualize.")
        return

    print(f"\n  Data ({size}): {data}")
    print(f"  Visualizing: {', '.join(selected)}\n")

    if len(selected) == 1:
        visualize_single(selected[0], data, interval=interval)
    else:
        visualize_compare(selected, data, interval=interval)

# ── Entry point ───────────────────────────────────────────────────────────────

if __name__ == "__main__":
    p = argparse.ArgumentParser(description="Sorting visualizer")
    p.add_argument("algos",    nargs="?", default=None,
                   help="number(s) or name(s), comma-separated: '1,3,7' or 'Bubble,Merge'")
    p.add_argument("--size",  "-s", type=int, default=20)
    p.add_argument("--speed",       type=int, default=40, help="ms per step")
    p.add_argument("--list", "-l",  action="store_true")
    args = p.parse_args()

    if args.list:
        _print_list()
        sys.exit(0)

    data = random.sample(range(1, args.size + 1), args.size)

    if args.algos:
        tokens   = [t.strip() for t in args.algos.split(",")]
        selected = _resolve(tokens)
        if not selected:
            print("No algorithms matched.")
            sys.exit(1)
        if len(selected) == 1:
            visualize_single(selected[0], data, interval=args.speed)
        else:
            visualize_compare(selected, data, interval=args.speed)
    else:
        menu()
