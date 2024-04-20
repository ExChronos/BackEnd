#5.1
#цена за 1-10 кг конфет
def five_one():
    price = 4.12

    for i in range(1, 10):
        print(f'Цена за {i} кг = {i*price}')
    
#5.2
#промежуток A & B
def five_two():
    A = int(input('Введите число A: '))
    B = int(input('Введите число B: '))

    if A < B:
        for i in range(A, B):
            if i % 2 == 0:
                print(i)
            else:
                pass
    elif A > B:
        for i in range(B, A):
            if i % 2 == 0:
                print(i)
            else:
                pass
    else:
        print(f'A = B')
    
#5.3
#вычислить сумму нескольких чисел

def five_three():
    import random

    nums = [random.randint(1,100) for i in range(21)]

    return sum(nums)

#5.4
#вычислить сумму факториалов N

def five_four():
    import math

    N = int(input('Введите число N(Сумма факториалов до N): '))
    factorials = [math.factorial(i) for i in range(1, N+1)]

    return sum(factorials)

#5.5
#вычислить количество дней оттепели

def five_five():
    import random

    N = int(input('Введите количество рассматриваемых дней (от 1 до 100): '))
    weather = [random.randint(-50, 50) for i in range(N)]
    hot = lambda x: x > 0 
    upper = [i for i in weather if hot(i)]

    for i in weather:
        print(i)

    return len(upper)

#5.6
#вычислить самый тяжелый и самый легкий арбузы

def five_six():
    import random

    N = int(input('Введите число арбузов: '))
    watermelons = [random.randint(1, 14) for i in range(N)]
    maxim = max(watermelons)
    minim = min(watermelons)

    return f'Тебе (максимальный вес): {maxim}, теще (минимальный вес): {minim}'

five_one()
five_two()
print(five_three())
print(five_four())
print(five_five())
print(five_six())

#6.1
#создание кортежа
def six_one():
    kort = (int(input('Введите число: ')) for i in range(5))
    print(kort, type(kort))

#6.2
#взятие элемента по индексу
def six_two():
    kort5 = (int(input('Введите число: ')) for i in range(5))
    item = kort5[2]
    print(item)

#6.3
#обращение к элементам
def six_three():
    s = 'strok'
    a = [1,2,3.4, 6e2, 'f']
    b = '1 2 3 4 5'
    c = '6 7 8 9 0'
    n = int(input('Введите число (от 0 до 2): '))
    k = 0
    if n == 2:
        k = int(input('Введите число (от 0 до 2): '))
    elif n < 2 and n >= 0:
        k = int(input('Введите число (от 0 до 4): '))

    my_tuple = (s, a, (b, c))

    print(my_tuple[n][k])

#6.4
#сравнение кортежей
def six_four():
    tup1 = (1,2,3)
    tup2 = (4,5,6)

    if len(tup1) > len(tup2):
        print(tup1[0])
    else:
        print(tup2[1])

#6.5
#срез кортежей
def six_five():
    tup = (1,2,3,4,5,6,7)
    print(tup[2])
    print(tup[len(tup)-1])
    print(tup[0:3])
    print(tup[::2])
    print(tup[1::2])
    print(tup[len(tup)::-1])

#6.6
#объединение кортежей
def six_six():
    my_tuple1 = (i for i in range(1,10,2))
    my_tuple2 = (i for i in range(0,10,2))
    n = int(input('Введите число n (повторения 1го кортежа): '))
    k = int(input('Введите число k (повторения 2го кортежа): '))

    my_tuple3 = n*my_tuple1+k*my_tuple2

    print(my_tuple3)

six_one()
six_two()
six_three()
six_four()
six_five()
six_six()