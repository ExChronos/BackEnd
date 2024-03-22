nums = []

for i in range(3):
    nums.append(int(input(f"Введите число {i}: ")))

def sum():
    summ = 0
    for i in nums:
        summ += i
    return summ

def mul():
    mull = 1
    for i in nums:
        mull *= i
    return mull

def aver():
    summ = sum()
    return summ/3

print(f'Сумма ваших чисел = {sum()}, перемножение = {mul()}, а среднее значение = {aver()}')