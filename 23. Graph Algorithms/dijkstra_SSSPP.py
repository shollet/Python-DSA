import heapq

class Edge:
    def __init__(self, weight, startVertex, targetVertex):
        self.weight = weight
        self.startVertex = startVertex
        self.targetVertex = targetVertex

class Node:
    def __init__(self, name):
        self.name = name
        self.visited = False
        self.predecessor = None
        self.neighbors = []
        self.minDistance = float("inf")
    
    def __lt__(self, otherNode):
        return self.minDistance < otherNode.minDistance
    
    def addEdge(self, weight, destinationVertex):
        edge = Edge(weight, self, destinationVertex)
        self.neighbors.append(edge)

class Dijkstra:
    def __init__(self):
        self.heap = []

    def calculate(self, startVertex):
        startVertex.minDistance = 0
        heapq.heappush(self.heap, startVertex)
        while self.heap:
            actualVertex = heapq.heappop(self.heap)
            if actualVertex.visited:
                continue
            for edge in actualVertex.neighbors:
                start = edge.startVertex
                target = edge.targetVertex
                newDistance = start.minDistance + edge.weight
                if newDistance < target.minDistance:
                    target.minDistance = newDistance
                    target.predecessor = start
                    heapq.heappush(self.heap, target)
            actualVertex.visited = True

    def getShortestPath(self, vertex):
        print(f"The shortest path to the vertex is: {vertex.minDistance}")
        actualVertex = vertex
        while actualVertex is not None:
            print(actualVertex.name, end=" ")
            actualVertex = actualVertex.predecessor

nodeA = Node("A")
nodeB = Node("B")
nodeC = Node("C")
nodeD = Node("D")
nodeE = Node("E")
nodeF = Node("F")
nodeG = Node("G")
nodeH = Node("H")

nodeA.addEdge(6, nodeB)
nodeA.addEdge(10, nodeC)
nodeA.addEdge(9, nodeD)

nodeB.addEdge(5, nodeD)
nodeB.addEdge(16, nodeE)
nodeB.addEdge(13, nodeF)

nodeC.addEdge(6, nodeD)
nodeC.addEdge(5, nodeH)
nodeC.addEdge(21, nodeG)

nodeD.addEdge(8, nodeF)
nodeD.addEdge(7, nodeH)

nodeE.addEdge(10, nodeG)

nodeF.addEdge(12, nodeG)
nodeF.addEdge(4, nodeE)

nodeH.addEdge(14, nodeG)
nodeH.addEdge(2, nodeF)

algorithm = Dijkstra()
algorithm.calculate(nodeA)
algorithm.getShortestPath(nodeB)
print()
algorithm.getShortestPath(nodeF)
print()
algorithm.getShortestPath(nodeG)