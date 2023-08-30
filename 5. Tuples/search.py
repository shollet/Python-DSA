newTuple = ('a', 'b', 'c', 'd', 'e')

print('a' in newTuple)
print('f' in newTuple)

print(newTuple.index('c'))
print(newTuple.index('e'))
#print(newTuple.index('f'))

def search(tuple, element):
    for i in range(len(tuple)):
        if  tuple[i] == element:
            return f"The element is found at index {i}"
    return 'The element is not found'

print(search(newTuple, 'b'))
print(search(newTuple, 'f'))