from QueueLinkedList import Queue

class AVLNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None
        self.height = 1

def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)

def inOrder(rootNode):
    if not rootNode:
        return
    inOrder(rootNode.leftChild)
    print(rootNode.data)
    inOrder(rootNode.rightChild)

def postOrder(rootNode):
    if not rootNode:
        return
    postOrder(rootNode.leftChild)
    postOrder(rootNode.rightChild)
    print(rootNode.data)

def levelOrder(rootNode):
    if not rootNode:
        return
    else:
        custQueue = Queue()
        custQueue.enqueue(rootNode)
        while not (custQueue.isEmpty()):
            root = custQueue.dequeue()
            print(root.value.data)
            if root.value.leftChild is not None:
                custQueue.enqueue(root.value.leftChild)
            if root.value.rightChild is not None:
                custQueue.enqueue(root.value.rightChild) 

def search(rootNode, target):
    if rootNode.data == target:
        print("The value is found")
    elif target < rootNode.data:
        if rootNode.leftChild.data == target:
            print("The value is found")
        else:
            search(rootNode.leftChild, target)
    else:
        if rootNode.rightChild.data == target:
            print("The value is found")
        else:
            search(rootNode.rightChild, target)

newAVL = AVLNode(10)