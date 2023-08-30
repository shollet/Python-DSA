from create import *
from insert import *

def deleteHeap(rootNode):
    rootNode.customList = None

newHeap = Heap(5)
inserNode(newHeap, 4, "Max")
inserNode(newHeap, 5, "Max")
inserNode(newHeap, 2, "Max")
inserNode(newHeap, 1, "Max")
deleteHeap(newHeap)
levelOrderTraversal(newHeap)