# XOR Sort - O(n²)
# Uses XOR swap trick (a ^= b; b ^= a; a ^= b) to swap elements without temp variable.
# Functionally identical to Bubble Sort but demonstrates the XOR swap.
# Note: XOR swap only works correctly when swapping different memory locations.
# Unstable | In-place | Classic bit manipulation trick

from data import *

def xor_sort(lista):
    lst = lista.copy()
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                # XOR swap - no temporary variable needed
                lst[j]     ^= lst[j + 1]
                lst[j + 1] ^= lst[j]
                lst[j]     ^= lst[j + 1]
    return lst

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(xor_sort(t))
