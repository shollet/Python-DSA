from operations import *

def getHeight(rootNode):
    if not rootNode:
        return 0
    return rootNode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftChild
    disbalanceNode.leftChild = disbalanceNode.leftChild.rightChild
    newRoot.rightChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightChild
    disbalanceNode.rightChild = disbalanceNode.rightChild.leftChild
    newRoot.leftChild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftChild), getHeight(disbalanceNode.rightChild))
    newRoot.height = 1 + max(getHeight(newRoot.leftChild), getHeight(newRoot.rightChild))
    return newRoot

def getBalance(rootNode):
    if not rootNode:
        return 0
    return getHeight(rootNode.leftChild) - getHeight(rootNode.rightChild)

def insert(rootNode, value):
    if not rootNode:
        return AVLNode(value)
    elif value < rootNode.data:
        rootNode.leftChild = insert(rootNode.leftChild, value)
    else:
        rootNode.rightChild = insert(rootNode.rightChild, value)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and value < rootNode.leftChild.data:
        return rightRotate(rootNode)
    if balance > 1 and value > rootNode.leftChild.data:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and value > rootNode.rightChild.data:
        return leftRotate(rootNode)
    if balance < -1 and value < rootNode.rightChild.data:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        leftRotate(rootNode)
    return rootNode

newAVL = AVLNode(5)
newAVL = insert(newAVL, 10)
newAVL = insert(newAVL, 15)
newAVL = insert(newAVL, 20)
# levelOrder(newAVL)