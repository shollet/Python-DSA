class Graph:
    def __init__(self, gdict=None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            self.gdict[vertex1].append(vertex2)
            self.gdict[vertex2].append(vertex1)
            return True
        return False

    def addVertex(self, vertex):
        if vertex not in self.gdict.keys():
            self.gdict[vertex] = []
            return True
        return False
    
    def printGraph(self):
        for vertex in self.gdict:
            print(vertex, ":", self.gdict[vertex])


graph = Graph()
graph.addVertex("A")
graph.addVertex("B")
graph.addEdge("A", "B")
graph.printGraph()