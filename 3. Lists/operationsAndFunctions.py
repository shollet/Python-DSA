a = [1,2,3]
b = [4,5,6]
c = a + b
print(c)

a = [0,1] * 4
print(a)

a = [0,1,2,3,4,5,6]
print(len(a))
print(max(a))
print(min(a))
print(sum(a) / len(a))

""" total = 0
count = 0
while (True):
    inp = input('Enter a number: ')
    if inp == 'done':
        break
    value = float(inp)
    total += value
    count += 1
    average = total / count """

def challenge():
    list = []
    while(True):
        inp = input('Enter a number: ')
        if inp == 'done':
            break
        value = float(inp)
        list.append(value)

    if len(list) != 0:
        print('Average:', sum(list) / len(list))
    else:
        print('Average: 0')

challenge()