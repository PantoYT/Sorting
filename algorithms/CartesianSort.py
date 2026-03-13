# Cartesian Tree Sort - O(n log n) average, O(n²) worst
# Builds a Cartesian tree (min-heap where in-order traversal = original order),
# then extracts minimum repeatedly (in-order traversal of the heap).
# Adaptive: O(n log k) when k sorted runs exist.
# Unstable | O(n) memory | Naturally adaptive

from data import *

class CartNode:
    __slots__ = ['val', 'left', 'right']
    def __init__(self, val):
        self.val = val
        self.left = self.right = None

def build_cartesian(lst):
    root = None
    stack = []
    for x in lst:
        node = CartNode(x)
        last = None
        while stack and stack[-1].val > x:
            last = stack.pop()
        if stack:
            stack[-1].right = node
        else:
            root = node
        node.left = last
        stack.append(node)
    return root

def cartesian_sort(lista):
    lst = lista.copy()
    if not lst:
        return lst
    root = build_cartesian(lst)
    result = []
    # extract via min-heap property: always extract root (min)
    import heapq
    heap = []
    def push(node):
        if node:
            heapq.heappush(heap, (node.val, id(node), node))
    push(root)
    while heap:
        _, _, node = heapq.heappop(heap)
        result.append(node.val)
        push(node.left)
        push(node.right)
    return result

if __name__ == "__main__":
    for t in [losowa, prawie_posort, odwrocona, duplikaty, duza]:
        print(cartesian_sort(t))
