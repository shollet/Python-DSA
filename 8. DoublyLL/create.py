class Node:
    def __init__(self, value=None):
        self.value = value
        self.prev = None
        self.next = None

class DoublyLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
        
    def create(self, value):
        node = Node(value)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The DLL is created successfully"
    
doublyLL = DoublyLL()
doublyLL.create(5)
print([node.value for node in doublyLL])