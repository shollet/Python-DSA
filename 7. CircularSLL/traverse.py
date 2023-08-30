class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

class CircularSLL:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            if node.next == self.head:
                break
            node = node.next

    def create(self, value):
        node = Node(value)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created"
    
    def insert(self, value, location):
        if self.head is None:
            return "The head reference is None"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been has been successfully inserted"
        
    def traverse(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

circularSLL = CircularSLL()
print(circularSLL.create(1))
circularSLL.insert(0,0)
circularSLL.insert(2,-1)
circularSLL.insert(3,-1)
circularSLL.insert(2,2)

circularSLL.traverse()