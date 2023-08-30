a = 'spam spam spam'
b = list(a)
print(b)

a = 'spam-spam-spam'
delimiter = '-'
b = a.split(delimiter)
print(b)
print(delimiter.join(b))