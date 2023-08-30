class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        newNode = Node(value)
        self.head = newNode
        self.tail = newNode
        self.length = 1

# class LinkedList:
#     def __init__(self):
#         self.head = None
#         self.tail = None
#         self.length = 0

newLinkedList = LinkedList(10)
print(newLinkedList.length)