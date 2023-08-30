from operations import *
from insert import *

def getMinValueNode(rootNode):
    if rootNode is None or rootNode.leftChild is None:
        return rootNode
    return getMinValueNode(rootNode.leftChild)

def delete(rootNode, value):
    if not rootNode:
        return rootNode
    elif value < rootNode.data:
        rootNode.leftChild = delete(rootNode.leftChild, value)
    elif value > rootNode.data:
        rootNode.rightChild = delete(rootNode.rightChild, value)
    else:
        if rootNode.leftChild is None:
            temp = rootNode.rightChild
            rootNode = None
            return temp
        if rootNode.rightChild is None:
            temp = rootNode.leftChild
            rootNode = None
            return temp
        temp = getMinValueNode(rootNode.rightChild)
        rootNode.data = temp.data
        rootNode.rightChild = delete(rootNode.rightChild, temp.data)

    rootNode.height = 1 + max(getHeight(rootNode.leftChild), getHeight(rootNode.rightChild))
    balance = getBalance(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) >= 0:
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) <= 0:
        return leftRotate(rootNode)
    if balance > 1 and getBalance(rootNode.leftChild) < 0:
        rootNode.leftChild = leftRotate(rootNode.leftChild)
        return rightRotate(rootNode)
    if balance < -1 and getBalance(rootNode.rightChild) > 0:
        rootNode.rightChild = rightRotate(rootNode.rightChild)
        return leftRotate(rootNode)
    return rootNode

newAVL = AVLNode(5)
newAVL = insert(newAVL, 10)
newAVL = insert(newAVL, 15)
newAVL = insert(newAVL, 20)
newAVL = delete(newAVL, 15)
levelOrder(newAVL)
