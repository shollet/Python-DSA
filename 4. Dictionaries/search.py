myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def search(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return f"The value {value} does not exist"

print(search(myDict, 55))