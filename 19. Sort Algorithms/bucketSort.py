from insertionSort import *
import math

def bucketSort(customList):
    numberofBuckets = round(math.sqrt(len(customList)))
    maxValue = max(customList)
    arr = []

    for _ in range(numberofBuckets):
        arr.append([])
    for value in customList:
        index = math.ceil(value * numberofBuckets / maxValue)
        arr[index-1].append(value)
    for n in range(numberofBuckets):
        arr[n] = insertionSort(arr[n])

    k = 0
    for i in range(numberofBuckets):
        for j in range(len(arr[i])):
            customList[k] = arr[i][j]
            k += 1
    return customList


print(bucketSort(cList))