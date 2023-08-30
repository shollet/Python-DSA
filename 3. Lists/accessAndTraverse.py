shoppingList = ['Milk', 'Cheese', 'Butter']
empty = []

for i in range(len(shoppingList)):
    shoppingList[i] += "+"
    print(shoppingList[i])

for i in empty:
    print("I am empty")