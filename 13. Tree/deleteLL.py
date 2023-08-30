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

def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            if (root.value.leftChild is not None):
                custQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                custQueue.enqueue(root.value.rightChild)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, dNode):
    if not rootNode:
        return
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value is dNode:
                root.value = None
                return
            if root.value.rightChild:
                if root.value.rightChild is dNode:
                    root.value.rightChild = None
                    return
                else:
                    custQueue.enqueue(root.value.rightChild)
            if root.value.leftChild:
                if root.value.leftChild is dNode:
                    root.value.leftChild = None
                    return
                else:
                    custQueue.enqueue(root.value.leftChild)

def delete(rootNode, node):
    if not rootNode:
        return "The BT does not exist"
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            if root.value.data == node:
                dNode = getDeepestNode(rootNode)
                root.value.data = dNode.data
                deleteDeepestNode(rootNode, dNode)
                return "The node has been successfully deleted"
            if (root.value.leftChild is not None):
                custQueue.enqueue(root.value.leftChild)
            if (root.value.rightChild is not None):
                custQueue.enqueue(root.value.rightChild)
        return "Failed to delete"

delete(newBT, 'Hot')
levelOrder(newBT)
