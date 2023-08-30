from search import *

def delete(root, word, index):
    ch = word[index]
    current = root.children.get(ch)
    canThisNodeBeDeleted = False

    if len(current.children) > 1:
        delete(current, word, index + 1)
        return False
    
    if index == len(word) - 1:
        if len(current.children) >= 1:
            current.endOfString = False
            return False
        else:
            root.children.pop(ch)
            return True
        
    if current.endOfString is True:
        delete(current, word, index + 1)
        return False
    
    canThisNodeBeDeleted = delete(current, word, index + 1)
    if canThisNodeBeDeleted is True:
        root.children.pop(ch)
        return True
    else:
        return False
    

delete(newTrie.root, "App", 0)
print(newTrie.search("App"))