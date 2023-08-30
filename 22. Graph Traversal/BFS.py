from collections import deque

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

    def removeEdge(self, vertex1, vertex2):
        if vertex1 in self.gdict.keys() and vertex2 in self.gdict.keys():
            try:
                self.gdict[vertex1].remove(vertex2)
                self.gdict[vertex2].remove(vertex1)
            except ValueError:
                pass
            return True
        return False
    
    def removeVertex(self, vertex):
        if vertex in self.gdict.keys():
            for otherVertex in self.gdict[vertex]:
                self.gdict[otherVertex].remove(vertex)
            del self.gdict[vertex]
            return True
        return False
    
    def bfs(self, vertex):
        visited = set()
        visited.add(vertex)
        queue = deque([vertex])
        while queue:
            current = queue.popleft()
            print(current)
            for otherVertex in self.gdict[current]:
                if otherVertex not in visited:
                    visited.add(otherVertex)
                    queue.append(otherVertex)

myGraph = Graph()
myGraph.addVertex("A")
myGraph.addVertex("B")
myGraph.addVertex("C")
myGraph.addVertex("D")
myGraph.addVertex("E")
myGraph.addEdge("A", "B")
myGraph.addEdge("A", "C")
myGraph.addEdge("B", "E")
myGraph.addEdge("C", "D")
myGraph.addEdge("D", "E")
myGraph.printGraph()
myGraph.bfs("A")