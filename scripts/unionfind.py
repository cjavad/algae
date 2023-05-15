
import pygraphviz as pgv
from tree import Tree
from IPython.display import Image

class UnionFind(Tree):
    def __init__(self, n):
        super().__init__()
        self.parent = [(i, 1) for i in range(n)]
        self.rank = [0] * n

    def find(self, p: int):
        if self.parent[p][0] != p:
            self.parent[p] = self.find(self.parent[p][0])  # path compression
        return self.parent[p]

    def union(self, p, q):
        root_p = self.find(p)
        root_q = self.find(q)
        if root_p == root_q: return

        if self.rank[root_p] < self.rank[root_q]:
            self.parent[root_p] = root_q
        elif self.rank[root_p] > self.rank[root_q]:
            self.parent[root_q] = root_p
        else:
            self.parent[root_q] = root_p
            self.rank[root_p] += 1

        self.count -= 1

if __name__ == "__main__":
    uf = UnionFind(22 + 1)
    uf.connect(0, 4)
    uf.connect(0, 2)
    uf.connect(0, 12)
    uf.connect(2, 1)
    uf.connect(1, 5)
    uf.connect(1, 10)
    uf.connect(5, 9)
    uf.connect(12, 13)
    uf.connect(12, 22)
    uf.connect(12, 14)
    uf.connect(14, 15)
    uf.connect(14, 16)
    uf.connect(14, 6)
    uf.connect(6, 7)
    uf.connect(6, 8)
    uf.connect(3, 17)
    uf.connect(17, 18)
    uf.connect(19, 20)
    uf.connect(19, 21)
    uf.connect(20, 11)

    print(uf.find(6)[0])
    print(f'total elements: {uf.count}')
    print(f'total leaves: {uf.total_leaves()}')
    print(f'max depth: {uf.max_depth()}')
    print(f'min depth: {uf.min_depth()}')
    print(f'max children: {uf.max_children()}')
    print(f'min children: {uf.min_children()}')

    uf.view()