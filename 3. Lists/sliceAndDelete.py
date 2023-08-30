myList = ['a', 'b', 'c', 'd', 'e', 'f']
print(myList)

myList[:2] = ['x', 'y']
myList.pop(1)
myList.pop()
del myList[0:2]
myList.remove('e')

print(myList)