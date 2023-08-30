from levelOrderLL import levelOrder
from QueueLinkedList import Queue

class TreeNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

def insert(rootNode, newNode):
    if not rootNode:
        rootNode = newNode
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)
            else:
                root.value.leftChild = newNode
                return "Successfully inserted"
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild)
            else:
                root.value.rightChild = newNode
                return "Successfully inserted"
            
cola = TreeNode("Cola")
print(insert(newBT, cola))

levelOrder(newBT)