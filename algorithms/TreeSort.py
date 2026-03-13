# Tree Sort - O(n log n) avg, O(n²) worst (unbalanced BST)
# Inserts all elements into a BST (Binary Search Tree),
# then traverses the tree in-order (left-root-right).
# Stable | O(n) memory

from data import *

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def insert(root, val):
    if root is None:
        return Node(val)
    if val <= root.val:
        root.left = insert(root.left, val)
    else:
        root.right = insert(root.right, val)
    return root

def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)

def tree_sort(lista):
    lst = lista.copy()
    root = None
    for x in lst:
        root = insert(root, x)
    result = []
    inorder(root, result)
    return result

if __name__ == "__main__":
    testy = [losowa, prawie_posort, odwrocona, jedna_roznica, duplikaty, duza, duza_losowa]
    for t in testy:
        print(tree_sort(t))
