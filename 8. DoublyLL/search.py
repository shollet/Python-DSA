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
    
    def insert(self, value, location):
        if self.head is None:
            print("The node cannot be inserted ")
        else:
            newNode = Node(value)
            if location == 0:
                newNode.prev = None
                newNode.next = self.head
                self.head.prev = newNode
                self.head = newNode
            elif location == -1:
                newNode.next = None
                newNode.prev = self.tail
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                newNode.next = tempNode.next
                newNode.prev = tempNode
                newNode.next.prev = newNode
                tempNode.next = newNode
    
    def traverse(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next

    def reverseTraversal(self):
        if self.head is None:
            print("There is not any element to traverse")
        else:
            tempNode = self.tail
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.prev

    def search(self, target):
        if self.head is None:
            return "There is not any element in DLL"
        else:
            tempNode = self.head
            while tempNode:
                if tempNode.value == target:
                    return tempNode.value
                tempNode = tempNode.next
            return "The node does not exist in this list"
        
doublyLL = DoublyLL()
doublyLL.create(5)
print([node.value for node in doublyLL])
doublyLL.insert(0,0)
doublyLL.insert(2,-1)
doublyLL.insert(6,2)
print([node.value for node in doublyLL])

print(doublyLL.search(5))
print(doublyLL.search(8))