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


def preOrder(rootNode):
    if not rootNode:
        return
    print(rootNode.data)
    preOrder(rootNode.leftChild)
    preOrder(rootNode.rightChild)

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
preOrder(newBST)

