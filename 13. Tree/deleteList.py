class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex + 1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def search(self, target):
        for i in range(len(self.customList)):
            if self.customList[i] == target:
                return "Success"
        return "Not found"
    
    def preOrder(self, index):
        if index > self.lastUsedIndex:
            return 
        print(self.customList[index])
        self.preOrder(index * 2)
        self.preOrder(index * 2 + 1)

    def inOrder(self, index):
        if index > self.lastUsedIndex:
            return 
        self.inOrder(index * 2)
        print(self.customList[index])
        self.inOrder(index * 2 + 1)

    def postOrder(self, index):
        if index > self.lastUsedIndex:
            return 
        self.postOrder(index * 2)
        self.postOrder(index * 2 + 1)
        print(self.customList[index])

    def levelOrder(self, index):
        for i in range(index, self.lastUsedIndex + 1):
            print(self.customList[i])

    def delete(self, value):
        if self.lastUsedIndex == 0:
            return "There is not any node to delete"
        for i in range(1, self.lastUsedIndex + 1):
            if self.customList[i] == value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return "The node has been successfully deleted"

newBT = BinaryTree(8)
newBT.insert("Drinks")
newBT.insert("Hot")
newBT.insert("Cold")
newBT.insert("Tea")
newBT.insert("Coffee")

print(newBT.delete("Hot"))
newBT.levelOrder(1)