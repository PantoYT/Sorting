"""
Automatyczny discovery algorytmów sortowania.
Każdy plik *Sort*.py w tym folderze jest importowany automatycznie.
Dodaj nowy algorytm = dodaj nowy plik. Zero hardcode.
"""
import os
import importlib
import inspect
import re

_dir = os.path.dirname(__file__)
_parent = os.path.dirname(_dir)

# słownik: nazwa_pliku -> funkcja_sortująca
REGISTRY = {}

def _is_sort_function(name, obj, module_name):
    if not callable(obj): return False
    if not inspect.isfunction(obj): return False
    # tylko funkcje z tego modułu (nie importowane)
    if obj.__module__ != f"algorithms.{module_name}": return False
    low = name.lower()
    # musi mieć "sort" w nazwie
    if "sort" not in low: return False
    # wyklucz helpery (insertion_sort_bucket, merge, heapify, itp.)
    skip = {"merge", "heapify", "flip", "sift", "trinkle", "insertion_sort_bucket",
            "is_sorted", "worker", "compare_and_swap", "sort3", "sort_quad",
            "sort_triple", "swap_if_needed", "counting_sort_by_digit", "merge_inplace",
            "bitonic_merge", "bitonic_sort_helper", "introsort_helper", "slow_sort",
            "stooge_sort_helper", "insert", "inorder", "partition", "bogosort"}
    if name in skip: return False
    return True

def _discover():
    for fname in sorted(os.listdir(_dir)):
        if not fname.endswith(".py"): continue
        if fname.startswith("_"): continue
        module_name = fname[:-3]
        try:
            mod = importlib.import_module(f"algorithms.{module_name}")
        except Exception:
            continue
        # znajdź główną funkcję sortującą
        funcs = [(n, obj) for n, obj in inspect.getmembers(mod)
                 if _is_sort_function(n, obj, module_name)]
        if not funcs:
            continue
        # preferuj nazwę najbliższą nazwie pliku
        file_lower = module_name.lower().replace("_", "")
        def score(nf):
            n, _ = nf
            return -len(os.path.commonprefix([n.lower(), file_lower]))
        funcs.sort(key=score)
        func_name, func = funcs[0]
        REGISTRY[module_name] = func

_discover()

# eksportuj wszystkie funkcje do przestrzeni nazw pakietu
for _mod_name, _func in REGISTRY.items():
    globals()[_func.__name__] = _func

__all__ = [f.__name__ for f in REGISTRY.values()]
