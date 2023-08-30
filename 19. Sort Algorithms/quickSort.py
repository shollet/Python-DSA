def swap(myList, index1, index2):
    temp = myList[index1]
    myList[index1] = myList[index2]
    myList[index2] = temp

def pivot(myList, pivotIndex, endIndex):
    swapIndex = pivotIndex
    for i in range(pivotIndex+1, endIndex+1):
        if myList[i] < myList[pivotIndex]:
            swapIndex += 1
            swap(myList, swapIndex, i)
    swap(myList, pivotIndex, swapIndex)
    return swapIndex

def quickSortHelper(myList, left, right):
    if left < right:
        pivotIndex = pivot(myList, left, right)
        quickSortHelper(myList, left, pivotIndex-1)
        quickSortHelper(myList, pivotIndex+1, right)
    return myList

def quickSort(myList):
    return quickSortHelper(myList, 0, len(myList)-1)


myList = [3,5,0,6,2,1,4]
print(pivot(myList, 0, 6))
print(quickSort(myList))