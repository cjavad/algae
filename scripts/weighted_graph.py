from graph import Graph

if __name__ == '__main__':
    g = Graph()
    
    g.connect(0, 1, 1)
    g.connect(0, 2, 6)
    g.connect(0, 4, 1)
    g.connect(0, 5, 2)
    g.connect(1, 2, 8)
    g.connect(2, 3, 14)
    g.connect(2, 5, 3)
    g.connect(3, 6, 1)
    g.connect(3, 7, 1)
    g.connect(4, 8, 7)
    g.connect(5, 6, 20)
    g.connect(5, 8, 3)
    g.connect(5, 9, 5)
    g.connect(5, 10, 8)
    g.connect(6, 7, 4)
    g.connect(6, 11, 8)
    g.connect(7, 11, 3)
    g.connect(8, 9, 4)
    g.connect(9, 10, 2)
    g.connect(10, 11, 5)

    t = g.minimum_spanning_tree()
    print(t.total_weight())
    t.view()