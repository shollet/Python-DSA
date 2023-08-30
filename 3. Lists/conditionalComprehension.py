prev_list = [-1, 10, -20, 2, -90, 60, 45, 20]
new_list = [number**2 for number in prev_list if number < 0]

print(new_list)

def isConsonant(letter):
    vowels = 'aeiouy'
    return letter.isalpha() and letter.lower() not in vowels

sentence = 'My name is Shayan'
consonants = [letter for letter in sentence if isConsonant(letter)]

print(consonants)

def getNumber(number):
    return number if number > 0 else 'negative number'

newList = [getNumber(number) for number in prev_list]
print(newList)
