import pygraphviz as pgv
from IPython.display import Image

from view import view_graphviz

class BinaryTree:
    def __init__(self, root):
        self.left = None
        self.right = None
        self.root = root

    def insert(self, new_node):
        if new_node < self.root:
            if self.left is None:
                self.left = BinaryTree(new_node)
            else:
                self.left.insert(new_node)
        else:
            if self.right is None:
                self.right = BinaryTree(new_node)
            else:
                self.right.insert(new_node)

    def search(self, key):
        if self.root == key:
            return True
        elif key < self.root:
            if self.left is None:
                return False
            else:
                return self.left.search(key)
        else:
            if self.right is None:
                return False
            else:
                return self.right.search(key)

    def delete(self, key):
        if key < self.root:
            if self.left is None:
                return False
            else:
                self.left = self.left.delete(key)
        elif key > self.root:
            if self.right is None:
                return False
            else:
                self.right = self.right.delete(key)
        else:
            if self.left is None:
                return self.right
            elif self.right is None:
                return self.left
            else:
                self.root = self.right.find_min()
                self.right = self.right.delete(self.root)
        return self

    def find_min(self):
        if self.left is None:
            return self.root
        else:
            return self.left.find_min()

    def find_max(self):
        if self.right is None:
            return self.root
        else:
            return self.right.find_max()
    
    def copy(self):
        if self.root is None:
            return None
        else:
            bst = BinaryTree(self.root)
            if self.left:
                bst.left = self.left.copy()
            if self.right:
                bst.right = self.right.copy()
            return bst
    
    @property
    def height(self):
        if self.root is None:
            return 0
        elif self.left is None and self.right is None:
            return 1
        elif self.left is None and (not self.right is None):
            return 1 + self.right.height
        elif self.right is None and (not self.left is None):
            return 1 + self.left.height
        else:
            return 1 + max(self.left.height, self.right.height)

    def to_graphviz(self, g=None):
        if g is None:
            g = pgv.AGraph(directed=True)

        # Add the current node
        g.add_node(self.root)

        if self.left:
            self.left.to_graphviz(g)
            g.add_edge(self.root, self.left.root)
        if self.right:
            self.right.to_graphviz(g)
            g.add_edge(self.root, self.right.root)

        return g

    def view(self):
        view_graphviz(self.to_graphviz())


if __name__ == "__main__":
    btree = BinaryTree(13)
    btree.insert(42)
    btree.insert(6)
    btree.insert(5)
    btree.insert(10)
    btree.insert(7)
    btree.insert(9)

    # Get height of the tree
    print(btree.height)
    btree.view()