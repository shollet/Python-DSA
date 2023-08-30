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
search(newBST, 60)