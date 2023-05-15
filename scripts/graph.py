from tree import Tree
from directed_graph import DirectedGraph
import pygraphviz as pgv
from scipy.sparse import csr_matrix
from scipy.sparse.csgraph import minimum_spanning_tree

class Graph(DirectedGraph):
    def __init__(self):
        super().__init__()

    def connect(self, a: int, b: int, weight: float=1):
        super().connect(a, b, weight)
        super().connect(b, a, weight)
    
    def to_graphviz(self, show_weight=False):
        g = pgv.AGraph()
        for i in range(len(self.edges)):
            for j, weight in self.edges[i]:
                kwargs = {} if not show_weight else {"label": weight}
                g.add_edge(i, j, **kwargs)

        return g

    