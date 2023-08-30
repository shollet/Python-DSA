class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

class CircularDLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break
    
    def create(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        newNode.prev = newNode
        newNode.next = newNode
        return "The CDLL is created successfully"
    
circularDLL = CircularDLL()
print(circularDLL.create(5))
print([node.value for node in circularDLL])