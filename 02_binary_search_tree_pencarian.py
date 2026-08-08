# Pencarian Elemen pada Binary Search Tree (BST)

class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(root, newValue):
    if root is None:
        root = BinaryTreeNode(newValue)
        return root
    if newValue < root.data:
        root.leftChild = insert(root.leftChild, newValue)
    else:
        root.rightChild = insert(root.rightChild, newValue)
    return root

def search(root, value):
    """
    Mencari nilai di dalam BST.
    Mengembalikan True jika ada, False jika tidak ada.
    """
    if root is None:
        return False
    if root.data == value:
        return True
    elif value < root.data:
        return search(root.leftChild, value)
    else:
        return search(root.rightChild, value)

if __name__ == "__main__":
    root = insert(None, 50)
    insert(root, 20)
    insert(root, 53)
    insert(root, 11)
    insert(root, 22)
    insert(root, 52)
    insert(root, 78)

    print("Hasil Pencarian di Binary Search Tree:")
    print("Apakah 53 ada di binary tree?", search(root, 53))
    print("Apakah 100 ada di binary tree?", search(root, 100))
