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

    def reverseTraversal(self):
        if self.head is None:
            print("There is not any element for traversal")
        else:
            temp = self.tail
            while temp:
                print(temp.value)
                if temp == self.head:
                    break
                temp = temp.prev

    def search(self, target):
        if self.head is None:
            return "There is not any element for searching"
        else:
            temp = self.head
            while temp:
                if temp.value == target:
                    return temp.value
                if temp == self.tail:
                    return "The value does not exist in CDLL"
                temp = temp.next

    def delete(self, location):
        if self.head is None:
            print("There is not any node in CDLL")
        else:
            if location == 0:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.head = self.head.next
                    self.head.prev = self.tail
                    self.tail.next = self.head
            elif location == -1:
                if self.head == self.tail:
                    self.head.prev = None
                    self.head.next = None
                    self.head = None
                    self.tail = None
                else:
                    self.tail = self.tail.prev
                    self.tail.next = self.head
                    self.head.prev = self.tail
            else:
                current = self.head
                index = 0
                while index < location - 1:
                    current = current.next
                    index += 1
                current.next = current.next.next
                current.next.prev = current
            print("The node has been successfully deleted")


circularDLL = CircularDLL()
print(circularDLL.create(5))
print([node.value for node in circularDLL])
circularDLL.insert(0,0)
circularDLL.insert(1,-1)
circularDLL.insert(2,2)
print([node.value for node in circularDLL])

circularDLL.delete(2)
print([node.value for node in circularDLL])
circularDLL.delete(0)
print([node.value for node in circularDLL])
circularDLL.delete(-1)
print([node.value for node in circularDLL])