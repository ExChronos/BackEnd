#4.1
#сумма чисел в массиве
def four_point_one():
    query = [i for i in range(12)]
    sum = 0

    for i in query:
        sum += i
    
    return sum


#4.2
#сумма чисел в трехзначном числе

def four_point_two():
    number = int(input('Введите трехзначное число: '))
    sum3 = 0

    for i in str(number):
        sum3 += int(i)

    return sum3

#4.3
#вывод степеней двойки меньше чем N

def four_point_three():
    N = int(input("Введите число N(Степени 2): "))
    k = 0
    num2 = 2**k

    while num2 < N:
        print(num2)
        k+=1
        num2 = 2**k

#4.4
#вычислить факториал числа N

def four_point_four():
    N = int(input('Введите число N(Факториал N): '))
    factor = 1
    i = 1

    while i <= N:
        factor *= i
        i+=1
    
    return f'{factor}\n'

#4.5
#вывести на экран числа кратные 7

def four_point_five():
    k = 1

    while k <= 14:
        print(7*k)
        k+=1
    print('\n')

#4.6
#вычислить сумму 5 произвольных чисел

def four_point_six():
    nums = []
    print("Сумма 5 чисел\n")

    for k in range(5):
        nums.append(int(input('Введите число: ')))
    
    return sum(nums)

print(four_point_one())
print(four_point_two())
four_point_three()
print(four_point_four())
four_point_five()
print(four_point_six())
