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

newBT = BinaryTree(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))
print(newBT.insert("Tea"))
print(newBT.insert("Coffee"))

newBT.inOrder(1)