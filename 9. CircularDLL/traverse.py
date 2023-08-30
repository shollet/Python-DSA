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
    
    def insert(self, value, location):
        if self.head is None:
            return "The CDLL does not exist"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.head
                newNode.prev = self.tail
                self.head.prev = newNode
                self.tail.next = newNode
                self.tail = newNode
            else:
                temp = self.head
                index = 0
                while index < location - 1:
                    temp = temp.next
                    index += 1
                newNode.next = temp.next
                newNode.prev = temp
                newNode.next.prev = newNode
                temp.next = newNode
            return "The node has been successfully inserted"
        
    def traverse(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            temp = self.head
            while temp:
                print(temp.value)
                if temp == self.tail:
                    break
                temp = temp.next

circularDLL = CircularDLL()
print(circularDLL.create(5))
print([node.value for node in circularDLL])
circularDLL.insert(0,0)
circularDLL.insert(1,-1)
circularDLL.insert(2,2)
print([node.value for node in circularDLL])

circularDLL.traverse()