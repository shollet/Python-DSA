myDict = {
    3: 'three',
    5: 'five',
    9: 'nine',
    2: 'two',
    1: 'one',
    4: 'four'
}

myDict1 = {
    0: 'zero',
    False: 'False',
    1: 'one'
}

print(3 in myDict)
print('three' in myDict)
print('three' in myDict.values())
print('three' not in myDict.values())
print('ten' not in myDict.values())

print(len(myDict))
print(all(myDict))
print(all(myDict1))
print(any(myDict))
print(any(myDict1))
print(sorted(myDict))