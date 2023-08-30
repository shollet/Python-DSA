myDict = {'name': 'Edy', 'age': 26, 'address': 'London', 'education': 'master'}

newDict = {'a': 1, 'b': 2, 'c': 3}
myDict.update(newDict)
print(myDict)

print(myDict.values())

print(myDict.pop('name1', 'not'))

print(myDict.setdefault('name1', 'added'))
print(myDict)

print(myDict.popitem())
print(myDict)

print(myDict.keys())

print(myDict.items())

print(myDict.get('city', 27))

newDict = {}.fromkeys([1,2,3], 0)
print(newDict)

dict = myDict.copy()
print(myDict)
print(dict)

myDict.clear()
print(myDict)