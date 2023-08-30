from array import *

myArray = array('i', [1,2,3,4,5,6,7,8,9])   # create

print("Step 1")

def traverse(array):                        # traverse
    for i in array:
        print(i)

traverse(myArray)

print("Step 2")

def access(array, index):                   # access
    if index >= len(array):
        print('Out of bond')
    else:
        print(array[index])

access(myArray, 8)

print("Step 3")

myArray.append(10)                          # append()
print(myArray)

print("Step 4")

myArray.insert(0, 0)                        # insert()
print(myArray)

print("Step 5")

myExtendedArray = array('i', [11,12,13])
myArray.extend(myExtendedArray)             # extend()
print(myArray)

print("Step 6")

myList = [14,15]
myArray.fromlist(myList)                    # fromlist()                     
print(myArray)

print("Step 7")

myArray.remove(0)
print(myArray)                              # remove()

print("Step 8")

myArray.pop()                               # pop()
print(myArray)

print("Step 9")

print(myArray.index(10))                    # index()

print("Step 10")

myArray.reverse()                           # reverse()
print(myArray)

print("Step 11")

print(myArray.buffer_info())                # buffer_info()

print("Step 12")

myOcurrencedArray = array('i', [1,1,1,1])
myArray.extend(myOcurrencedArray)
print(myArray.count(1))                     # count()

print("Step 13")

strArray = myArray.tobytes()
print(strArray)                             # tobytes()
ints = array('i')
ints.frombytes(strArray)
print(ints)

print("Step 14")

print(myArray.tolist())                     # tolist()

print("Step 15")

def slice(array, start, end):
    return array[start:end]
print(slice(myArray, 2, 8))                 # slice