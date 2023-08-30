from collections import defaultdict

class Graph:
    def __init__(self, numberofVertices):
        self.graph = defaultdict(list)
        self.numberofVertices = numberofVertices

    def addEdge(self, vertex, edge):
        self.graph[vertex].append(edge)

    def topologicalSortUtil(self, v, visited, stack):
        visited.append(v)

        for i in self.graph[v]:
            if i not in visited:
                self.topologicalSortUtil(i, visited, stack)
        stack.insert(0,v)

    def topologicalSort(self):
        visited = []
        stack = []

        for k in list(self.graph):
            if k not in visited:
                self.topologicalSortUtil(k, visited, stack)
        print(stack)

myGraph = Graph(8)
myGraph.addEdge("A", "C")
myGraph.addEdge("C", "E")
myGraph.addEdge("E", "H")
myGraph.addEdge("E", "F")
myGraph.addEdge("F", "G")
myGraph.addEdge("B", "C")
myGraph.addEdge("B", "D")
myGraph.addEdge("D", "F")
myGraph.topologicalSort()