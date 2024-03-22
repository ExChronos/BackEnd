import math

def var5():
    a = 0.7
    b = 0.05
    x = 0.5

    y = (pow(x, 2)*(x+1))/b - pow((math.sin(x+a)), 2)

    return y


print(var5())

def var7():
    a = 1.1
    b = 0.004
    x = 0.2

    y = pow(math.sin(pow((pow(x, 2)+a), 2)), 3) - math.sqrt(x//b)

    return y

print(var7())