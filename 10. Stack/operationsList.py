class Stack:
    def __init__(self):
        self.list = []

    def __str__(self):
        values = self.list.reverse()
        values = [str(x) for x in self.list]
        return "\n".join(values)
    
    def isEmpty(self):
        if self.list == []:
            return True
        else:
            return False
        
    def push(self, value):
        self.list.append(value)
        return "The element has been successfully inserted"
    
    def pop(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list.pop()
        
    def peek(self):
        if self.isEmpty():
            return "The stack is empty"
        else:
            return self.list[-1]
        
    def delete(self):
        self.list = None
        
customStack = Stack()
print(customStack.isEmpty())
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack.pop())
print(customStack.peek())