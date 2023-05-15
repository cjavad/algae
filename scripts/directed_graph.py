from tree import Tree
import pygraphviz as pgv
from IPython.display import Image
from view import view_graphviz
import heapq
from typing import List, Any

class DirectedGraph:
    def __init__(self):
        self.vertices: List[Any] = []
        self.edges: List[List[(int, float)]] = []

    def insert(self, i: int, vertex):
        self.vertices.extend([None]*(i + 1 - len(self.vertices)))
        self.vertices[i] = vertex

    def vertex(self, i: int):
        if len(self.vertices) > i:
            return self.vertices[i]
        else:
            return None
    
    def connect(self, a: int, b: int, weight: float = 1):
        while len(self.edges) < (a + 1):
            self.edges.append([])
        
        self.edges[a].append((b, weight))

    def bfs_tree(self, start=0):
        tree = Tree()
        tree.connect(start, start)
        tree.insert(start, self.vertex(start))

        visited = [start]
        queue = [start]
        
        while len(queue) > 0:
            i = queue.pop(0)

            self.edges[i].sort(key=lambda x: x[0])
            for child, weight in self.edges[i]:
                if child in visited:
                    continue
                
                tree.connect(i, child, weight)
                tree.insert(i, self.vertex(i))
                
                queue.append(child)
                visited.append(child)
                
        return tree
    
    def dfs_tree(self, start=0):
        tree = Tree()
        tree.connect(start, start)
        tree.insert(start, self.vertex(start))

        visited = []
        stack = [start]

        while len(stack) > 0:
            i = stack.pop()
            visited.append(i)

            self.edges[i].sort(reverse=True, key=lambda x: x[0])
            for child, weight in self.edges[i]:
                if child in visited:
                    continue

                tree.connect(i, child, weight)
                tree.insert(i, self.vertex(i))
                
                stack.append(child)

        return tree
    
    def minimum_spanning_tree(self, start=0):
        tree = Tree()
        visited = set()
        priority_queue = [(0, start, start)]  # (weight, source, destination)

        while priority_queue:
            weight, i, j = heapq.heappop(priority_queue)

            if j not in visited:
                tree.connect(i, j, weight)
                tree.insert(j, self.vertex(j))
                visited.add(j)

                for child, child_weight in self.edges[j]:
                    if child not in visited:
                        heapq.heappush(priority_queue, (child_weight, j, child))

        return tree

    def to_graphviz(self, show_weight=False):
        g = pgv.AGraph(directed=True)
        for i in range(len(self.edges)):
            for j, weight in self.edges[i]:
                kwargs = {} if not show_weight else {"label": weight}
                g.add_edge(i, j, **kwargs)

        return g
    
    def view(self, show_weight=False):
        view_graphviz(self.to_graphviz(show_weight))

if __name__ == "__main__":
    g = DirectedGraph()
    g.connect(0, 2)
    g.connect(0, 5)
    g.connect(0, 4)
    g.connect(1, 0)
    g.connect(2, 1)
    g.connect(2, 3)
    g.connect(3, 6)
    g.connect(4, 8)
    g.connect(5, 6)
    g.connect(5, 8)
    g.connect(5, 9)
    g.connect(5, 10)
    g.connect(7, 6)
    g.connect(9, 8)
    g.connect(9, 10)
    g.connect(10, 11)
    g.connect(11, 6)
    g.connect(11, 7)
    g.view()

    bfs_tree = g.bfs_tree(0)
    dfs_tree = g.dfs_tree(0)

    print(f'leaves: {bfs_tree.total_leaves()}')
    print(f'leaves: {dfs_tree.total_leaves()}')

    bfs_tree.view()
    dfs_tree.view()