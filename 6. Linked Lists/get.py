class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        tempNode = self.head
        result = ''
        while tempNode is not None:
            result += str(tempNode.value)
            if tempNode.next is not None:
                result += ' -> '
            tempNode = tempNode.next
        return result
    
    def append(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        self.length += 1

    def prepend(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            newNode.next = self.head
            self.head = newNode
        self.length += 1

    def insert(self, index, value):
        if index == 0:
            self.prepend(value)
        elif index < 0  or index > self.length:
            return False
        else:
            newNode = Node(value)
            tempNode = self.head
            for _ in range(index - 1):
                tempNode = tempNode.next
            newNode.next = tempNode.next
            tempNode.next = newNode
            self.length += 1
            return True
        
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next

    def search(self, target):
        current = self.head
        index = 0
        while current:
            if current.value == target:
                return index
            current = current.next
            index += 1
        return -1
    
    def get(self, index):
        if index == -1:
            return self.tail.value
        elif index < 0 or index >= self.length:
            return None
        else:
            current = self.head
            for _ in range(index):
                current = current.next
            return current.value
    

newLinkedList = LinkedList()
newLinkedList.insert(0, 50)
print(newLinkedList)
newLinkedList.insert(-4, 50)
newLinkedList.insert(7, 70)
print(newLinkedList)
newLinkedList.prepend(10)
newLinkedList.append(70)
newLinkedList.append(30)
print(newLinkedList)
newLinkedList.prepend(40)
print(newLinkedList)
newLinkedList.insert(0, 50)
print(newLinkedList)
newLinkedList.traverse()
print(newLinkedList.search(30))
print(newLinkedList.search(60))
print(newLinkedList.get(2))
print(newLinkedList.get(-1))
print(newLinkedList.get(6))