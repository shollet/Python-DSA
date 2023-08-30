myList = [2,4,3,1,5,7]
orig = myList[:]

mysortedList = myList.sort()
print(mysortedList)

# myList.append([10])
myList += [10]


print(sorted(orig))
print(orig)
