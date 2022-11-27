#Задача 334

a = 2
b = 5
c = 0
d = 2
for i in range(a, b, c + 1):
    if i%d==c:
        print(i)

#Задача 3642

i = 1
while i<7:
    print(i*i, end=' ')
    i+=1

#Задача 3644
N = 50
for i in range(0, 50):
    if 2**i < 50:
        print(2**i, end=' ')

#Задача 3647

x = 10
y = 20
d = 1
while x<y:
    x=x*1.1
    d=d+1
print(d)

#Задача 3533

i = 3
for i in range(i,i+1):
    i+=3
    print(i)

#Задача 3535

n = 3
a = '   _~_    '
b = '  (o o)   '
c = ' /  V  \  '
d = '/(  _  )\ '
e = '  ^^ ^^   '
print(a*n)
print(b*n)
print(c*n)
print(d*n)
print(e*n)

