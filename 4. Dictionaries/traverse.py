myDict = {'name': 'Edy', 'age': 26, 'address': 'London'}

def traverse(dict):
    for key in dict:
        print(key, dict[key])

traverse(myDict)