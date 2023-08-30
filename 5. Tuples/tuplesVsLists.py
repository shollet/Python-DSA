list1 = [0,1,2,3,4,5,6,7]
tuple1 = 0,1,2,3,4,5,6,7

list1[1] = 3
#tuple[1] = 3
print(list1)

list1 = [7,6,5,4,3,2,1,0]
tuple1 = 7,6,5,4,3,2,1,0
print(list1)
print(tuple1)

del list1[0]
#del tuple1[0]
print(list1)

list1 = [(1,2), (9,0), (3,4)]
tuple1 = ([1,2], [9,0], [3,4])
print(list1)
print(tuple1)

list1 = [[1,2], [9,0], [3,4]]
tuple1 = ((1,2), (9,0), (3,4))
print(list1)
print(tuple1)
