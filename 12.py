#one - первая функция

one = lambda x, y: x/y if y!=0 else print(f'dev 0 - {y/x}')

#two - вторая функция

gl = ['a', 'e', 'i', 'o', 'u']
glR = ['а', "е", "ё", "и", "о", "у", "ы", "э", "ю", "я"]

str = input('Введите строку: ')
count = 0
two = lambda let: 1 if(let in gl or let in glR) else 0
for i in str:
    count += two(i)
    
#three - третья функция

three = lambda x, y: x if x > y else y

#four - четвертая функция

lis = [1,2,3,4,5,6,7,8,9]

four = list(map(lambda x: x+10, lis))

# five

def fiveS():
    import math
    global lis
    
    
    five = list(map(lambda x: math.sqrt(x), lis))
    
    print(five)
    
#six

lis1 = [0,-1,0,2,-2,5,-3]

six = set(filter(lambda x: x>=0, lis1))


#seven

seven = set(filter(lambda x: x%3==0, lis1))

print(seven)