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

def search(rootNode, value):
    if not rootNode:
        return "The BT does not exist"
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not(custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.data == value:
                return "Success"
            if (root.value.leftChild is not None):
                custQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                custQueue.enqueue(root.value.rightChild)
        return "Not found"
    
newBT = TreeNode("Drinks")
leftChild = TreeNode("Hot")
tea = TreeNode("Tea")
coffee = TreeNode("Coffee")
leftChild.leftChild = tea
leftChild.rightChild = coffee
rightChild = TreeNode("Cold")
newBT.leftChild = leftChild
newBT.rightChild = rightChild

print(search(newBT, "Cola"))

