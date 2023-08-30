def selectionSort(customList):
    for i in range(len(customList)):
        min = i
        for j in range(i+1, len(customList)):
            if customList[min] > customList[j]:
                min = j
        customList[i], customList[min] = customList[min], customList[i]
    print(customList)

cList = [2,1,7,6,5,3,4,9,8]
selectionSort(cList)