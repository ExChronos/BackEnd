def task1():
    import random
    num = random.randint(1,10)
    user = int(input('Введите число: '))
    
    if user == num:
        print('Вы угадали')
    else:
        while user != num:
            user=int(input('Введите число: '))

def task2():
    
    lets = set()
    exist = dict()
    string = input('Введите строку: ')
    
    for let in string:
        
        if let in lets:
            exist[let] += 1
        else:
            lets.add(let)
            exist[let]=1
    return exist.items()

def task3():
    elem = input('Введите элемент')
    if elem in [1,2,3,4,5,'asdf','mama']:
        print('Найден')
    else:
        print('Не найден')

def task4():
    lis = [1,2,1,1,2,2,3,4,3,2,3,'mama','mama','papa']
    print(set(lis))
    
def task5(n):

    if n == 1:
        return 1
    else:
        return n*task5(n-1)
    
print(task5(10))