import time
from random import choice as ch
c = 0
v = [0]*10000 + [1]*1

n = time.time()
for i in range(100000):
    p = ch(v)
    if p==0:
        c += 1
    else:
        c += 1//p

print("{} ms elapsed".format((time.time()-n)*1000))
print(c)

c = 0
n = time.time()
for i in range(100000):
    p = ch(v)
    try:
        c += 1//p
    except:
        c += 1

print("{} ms elapsed".format((time.time()-n)*1000))
print(c)
