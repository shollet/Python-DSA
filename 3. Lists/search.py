myList = [10,20,30,40,50,60,70,80,90]
target = 90

# in operator

if target in myList:
    print(f"{target} is in the list")
else:
    print(f"{target} is not in the list")

# linear search

def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(linear_search(myList, target))