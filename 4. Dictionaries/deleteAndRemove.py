myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

del myDict['age']
print(myDict)

removedElem = myDict.pop('agee', None)

print(removedElem)
print(myDict)

removedElem2 = myDict.popitem()
print(removedElem2)
print(myDict)

myDict.clear()
print(myDict)