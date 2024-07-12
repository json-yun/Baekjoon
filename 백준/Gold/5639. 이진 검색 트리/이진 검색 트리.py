from __future__ import annotations
import sys

sys.setrecursionlimit(100000)

class Node:
    def __init__(self, key: any, value: any=None, left: Node=None, right: Node=None) -> None:
        self.key = key
        self.value = value
        self.left = left
        self.right = right
    def __repr__(self) -> str:
        return self.value if self.value else self.key

class BinarySearchTree:
    def __init__(self, root: Node | None=None) -> None:
        self.root = self.current = root
    
    def preorder(self, root: Node) -> list:
        result = []
        result += [root.key]
        if root.left:
            result += self.preorder(root.left)
        if root.right:
            result += self.preorder(root.right)
        return result
    
    def inorder(self, root: Node) -> list:
        result = []
        if root.left:
            result += self.inorder(root.left)
        result += [root.key]
        if root.right:
            result += self.inorder(root.right)
        return result
    
    def postorder(self, root: Node) -> list:
        result = []
        if root.left:
            result += self.postorder(root.left)
        if root.right:
            result += self.postorder(root.right)
        result += [root.key]
        return result

    def search(self, key: any) -> Node:
        current = self.root
        while current is not None:
            if current.key > key:
                if current.left is not None:
                    current = current.left
                else:
                    break
            elif current.key < key:
                if current.right is not None:
                    current = current.right
                else:
                    break
            else:
                break
        return current
    
    def insert(self, node: Node) -> None:
        next = self.search(node.key)
        if next is None:
            self.root = node
        elif next.key < node.key:
            next.right = node
        elif next.key > node.key:
            next.left = node
    
def main() -> None:
    N = [int(i) for i in sys.stdin]
    N.reverse()
    
    tree = BinarySearchTree()
    while N:
        tree.insert(Node(N.pop()))
    print("\n".join(map(str, tree.postorder(tree.root))))
        
    
main()