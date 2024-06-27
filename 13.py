import time, random, rsa

def one():
    start = time.time()
    num = random.randint(1,100)
    stop = time.time()
    time = stop-start
    print(time)
    

def two():
    num = random.randint(1,100)
    
    start = time.time()
    n = int(input('Введите число: '))
    
    while n != num:
        if n < num:
            print(f'{n} меньше чем нужно')
        else:
            print(f'{n} больше чем нужно')

        n = int(input('Введите снова: '))
    end = time.time()
    duration = str(end - start)[:4]
    
    print(f'Вы угадали за {duration} секунд')
    
def three():   
    start = time.time()
    
    lis = ['one', 2, 'tres', 'Spt', 'Bro']
    elem = random.choice(lis)
    
    end = time.time()
    
    duration = end - start
    return duration
    
time = three()
print(time)

def five():
    publicKey, privatKey = rsa.newkeys(512)
    
    msg = b'Hello teacher'
    crypto = rsa.encrypt(msg, publicKey)
    mess = rsa.decrypt(crypto, privatKey)
    
    print(mess)
    
five()