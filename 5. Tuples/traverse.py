newTuple = ('a', 'b', 'c', 'd', 'e')

def traverse(tuple):
    for i in tuple:
        print(i)
    for i in range(len(tuple)):
        print(tuple[i])


traverse(newTuple)