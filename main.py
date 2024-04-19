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
