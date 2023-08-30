from operations import *
from insert import *

def deleteAVL(rootNode):
    rootNode.data = None
    rootNode.leftChild = None
    rootNode.rightChild = None
    return "The AVL has been successfully deleted"

newAVL = AVLNode(5)
newAVL = insert(newAVL, 10)
newAVL = insert(newAVL, 15)
newAVL = insert(newAVL, 20)
deleteAVL(newAVL)
levelOrder(newAVL)