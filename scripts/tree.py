
import pygraphviz as pgv
from view import view_graphviz

class Tree:
    def __init__(self):
        self.parent = []
        self.vertices = []

    def insert(self, i: int, vertex):
        self.vertices.extend([None]*(i + 1 - len(self.vertices)))
        self.vertices[i] = vertex
    
    def vertex(self, i: int):
        if len(self.vertices) > i:
            return self.vertices[i]
        else:
            return None
    
    def connect(self, p: int, q: int, weight: float = 1):
        while len(self.parent) < q + 1:
            self.parent.append(None)
            
        self.parent[q] = (p, weight)

    def connected(self, p: int, q: int):
        return self.parent[q][0] == p if len(self.parent) > q and self.parent[q] != None else False or self.parent[p][0] == q if len(self.parent) > p and self.parent[p] != None else False

    @property
    def count(self):
        return len(self.parent)

    def total_leaves(self):
        counts = [0]*len(self.parent)
        for parent, _ in self.parent:
            counts[parent] += 1

        # Leaves are nodes with no children
        return counts.count(0)

    def max_depth(self):
        depths = [0]*len(self.parent)
        for i in range(len(self.parent)):
            j = i
            while self.parent[j][0] != j:
                depths[i] += 1
                j = self.parent[j][0]

        return max(depths)

    def min_depth(self):
        depths = [0]*len(self.parent)
        for i in range(len(self.parent)):
            j = i
            while self.parent[j][0] != j:
                depths[i] += 1
                j = self.parent[j][0]

        return min(depths)

    def max_children(self):
        counts = [0]*len(self.parent)
        for parent, _ in self.parent:
            counts[parent] += 1

        return max(counts)

    def min_children(self):
        counts = [0]*len(self.parent)
        for parent, _ in self.parent:
            counts[parent] += 1
        counts = [x for x in counts if x != 0]
        return min(counts)
    
    def total_weight(self):
        s = 0
        for n in self.parent:
            s += n[1] if n is not None else 0
        return s

    def to_graphviz(self, show_weight=False):
        g = pgv.AGraph(directed=True)

        for i in range(len(self.parent)):
            if self.parent[i] is None:
                continue

            g.add_node(i)
            parent, weight = self.parent[i]

            kwargs = {} if not show_weight else {"label": weight}
            g.add_edge(i, parent, **kwargs)

        return g

    def view(self, show_weight=False):
        view_graphviz(self.to_graphviz(show_weight=show_weight))