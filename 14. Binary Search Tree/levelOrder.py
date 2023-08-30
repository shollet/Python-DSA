from QueueLinkedList import Queue

class BSTNode:
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

def insert(rootNode, value):
    if rootNode.data == None:
        rootNode.data = value
    elif value <= rootNode.data:
        if rootNode.leftChild is None:
            rootNode.leftChild = BSTNode(value)
        else:
            insert(rootNode.leftChild, value)
    else:
        if rootNode.rightChild is None:
            rootNode.rightChild = BSTNode(value)
        else:
            insert(rootNode.rightChild, value)
    return "The node has been successfully inserted"


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

newBST = BSTNode(None)
insert(newBST, 70)
insert(newBST, 50)
insert(newBST, 90)
insert(newBST, 30)
insert(newBST, 60)
insert(newBST, 80)
insert(newBST, 100)
insert(newBST, 20)
insert(newBST, 40)
levelOrder(newBST)