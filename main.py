#1

string = 'have a nice day'

mas = string.split(' ')
newmas = mas[::-1]
newstring = ''

for i in newmas:
    newstring += i+' '

print(newstring)
