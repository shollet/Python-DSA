class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfString = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                node = TrieNode()
                current.children.update({ch: node})
            current = node
        current.endOfString = True
        print("Successfully inserted")

    def search(self, word):
        current = self.root
        for i in word:
            ch = i
            node = current.children.get(ch)
            if node is None:
                return False
            current = node
        return current.endOfString
    
newTrie = Trie()
newTrie.insert("App")
newTrie.insert("Appl")
# print(newTrie.search("DCD"))