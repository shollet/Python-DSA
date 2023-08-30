class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        current = self.head
        while current:
            yield current
            current = current.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)
    
    def enqueue(self, value):
        newNode = Node(value)
        if self.linkedList.head is None:
            self.linkedList.head = newNode
            self.linkedList.tail = newNode
        else:
            self.linkedList.tail.next = newNode
            self.linkedList.tail = newNode

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False
        
    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            temp = self.linkedList.head
            if self.linkedList.head == self.linkedList.tail:
                self.linkedList.head = None
                self.linkedList.tail = None
            else:
                self.linkedList.head = self.linkedList.head.next
            return temp
        
    def peek(self):
        if self.isEmpty():
            return "The queue is empty"
        else:
            return self.linkedList.head
        
    def delete(self):
        self.linkedList.head = None
        self.linkedList.head = None
        

custQueue = Queue()
custQueue.enqueue(1)
custQueue.enqueue(2)
custQueue.enqueue(3)
print(custQueue)
print(custQueue.dequeue())
print(custQueue)
print(custQueue.peek())