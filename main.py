import math
#3.1

num = int(input('Введите число: '))

if num > 0:
    print('Положительное')
elif num < 0:
    print('Отрицательное')
else:
    print('Zero')

#3.2
    
a = 2.5
x = float(input('Введите число: '))

def ret(x, a):
    y = 0

    if x > a:
        y = x * math.pow(x-a, 1/3)
    elif x == a:
        y = x * math.sin(a*x)
    else:
        y = math.exp(-a*x) * math.cos(a*x)

    return y

print(ret(x, a))