import random

num = random.randrange(100, 999)
snum = ''

for i in str(num):
    snum += f'{i},'

snum = snum[:len(snum)-1]

print(snum)