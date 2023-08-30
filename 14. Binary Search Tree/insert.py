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

newBST = BSTNode(None)
print(insert(newBST, 70))
print(insert(newBST, 60))
print(newBST.data)
print(newBST.leftChild.data)