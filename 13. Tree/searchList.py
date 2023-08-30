class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxSize = size

    def insert(self, value):
        if self.lastUsedIndex + 1 == self.maxSize:
            return "The Binary Tree is full"
        self.customList[self.lastUsedIndex+1] = value
        self.lastUsedIndex += 1
        return "The value has been successfully inserted"
    
    def search(self, target):
        for i in range(len(self.customList)):
            if self.customList[i] == target:
                return "Success"
        return "Not found"

newBT = BinaryTree(8)
print(newBT.insert("Drinks"))
print(newBT.insert("Hot"))
print(newBT.insert("Cold"))

print(newBT.search("Tea"))
print(newBT.search("Hot"))