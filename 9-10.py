def task1(args=[0]):
    return (sum(args)/len(args))

def task2():
    import math
    S1 = S2 = S3 = 0
    for i in range(3):
        a = int(input('Сторона a\n'))
        b = int(input('Сторона b\n'))
        c = int(input('Сторона c\n'))
        p = (a+b+c)/2
        S = math.sqrt(p*(p-a)*(p-b)*(p-c))
        if i == 0: S1 = S
        elif i == 1: S2 = S
        elif i == 2: S3 = S
    return S1 == S2 == S3
        
def task3(A,B,C):
    if A==B==C==0:
        return 'В центре координат'
    elif A!=0:
        return 1
    elif B!=0:
        return 2
    else:
        return 3
    
def task4():
    k = int(input('k: '))
    pos = []
    neg = []
    for i in range(k):
        num = int(input('num: '))
        if num > 0:
            pos.append(num)
        else:
            neg.append(num)
        
    print(f'{len(pos)} positive, {len(neg)} negative')
    
def task51(a,b):
    mas = []
    
    for i in range(a,b):
        mas.append(i)
    return mas

def task52():
    return sum(task51(4,10))

def task61(b):
    import math
    return (math.sqrt(i) for i in range(1,b+1))

def task62():
    import statistics
    return statistics.mean(task61(4))

def task7(args):
    max1 = max(args)
    args.remove(max1)
    max2 = max(args)
    return max1+max2
    
def task8(args):
    max1=max(args)
    min1=min(args)
    args.remove(max1)
    args.remove(min1)
    print(*args)

def task9(args):
    more = len([x for x in args if (lambda x: x > 0)])
    less = len([x for x in args if (lambda x: x < 0)])
    return f'{more} больше 0, {less} меньше нуля'

def task10(args):
    grade = int(input('Оценка (0 - завершить)'))
    five = 0
    disc = 0
    
    while grade:
        if grade == 5:
            five += 1
        
    if 4 <= five <= 5:
        disc = 10
    elif five > 5:
        disc=15
    else:
        disc=0
    return f'Скидка на билеты в театр - {disc}%'

            