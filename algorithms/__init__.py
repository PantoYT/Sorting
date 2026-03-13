"""
Auto-discovery of sorting algorithms.
Every *Sort*.py file in this directory is imported automatically.
Adding a new algorithm = adding a new file. Zero hardcoding.
"""
import os
import importlib
import inspect

_dir    = os.path.dirname(os.path.abspath(__file__))

REGISTRY: dict[str, callable] = {}

_HELPER_NAMES = frozenset({
    "merge", "heapify", "flip", "sift", "trinkle", "insertion_sort_bucket",
    "is_sorted", "worker", "compare_swap", "compare_and_swap", "sort3",
    "sort_quad", "sort_triple", "swap_if_needed", "counting_sort_by_digit",
    "merge_inplace", "bitonic_merge", "bitonic_sort_helper", "introsort_helper",
    "slow_sort", "stooge_sort_helper", "insert", "inorder", "partition",
    "bogosort", "build_cartesian", "push", "rotate", "weave",
    "generate_batcher_network", "count_inversions_approx",
    "fitness", "crossover", "mutate", "parallel_sort",
})

def _pick_main_function(mod, module_name: str):
    """Return the primary sort function from a module."""
    candidates = []
    mod_qname = f"algorithms.{module_name}"
    for name, obj in inspect.getmembers(mod, inspect.isfunction):
        if obj.__module__ != mod_qname:
            continue
        if "sort" not in name.lower():
            continue
        if name in _HELPER_NAMES:
            continue
        candidates.append(name)
    if not candidates:
        return None, None
    # prefer name closest to file name
    base = module_name.lower().replace("_", "")
    candidates.sort(key=lambda n: -len(os.path.commonprefix([n.lower(), base])))
    name = candidates[0]
    return name, getattr(mod, name)

def _discover():
    for fname in sorted(os.listdir(_dir)):
        if not fname.endswith(".py") or fname.startswith("_"):
            continue
        module_name = fname[:-3]
        try:
            mod = importlib.import_module(f"algorithms.{module_name}")
        except Exception:
            continue
        func_name, func = _pick_main_function(mod, module_name)
        if func is not None:
            REGISTRY[module_name] = func
            globals()[func_name] = func

_discover()

__all__ = list(REGISTRY.keys()) + ["REGISTRY"]
