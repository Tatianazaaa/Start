#Задача 3791

def distance(x1, y1, x2, y2):
    return ((x1-x2)**2+(y1-y2)**2)**0.5
x1 = 0
y1 = 0
x2 = 1
y2 = 1
print(distance(x1, y1, x2, y2))

#Задача 3790

def min4(a, b, c, d):
    return min(a, b, c, d)
a = 4
b = 5
c = 6
d = 7
print(min4(a, b, c, d))

# Калькулятор

a = int(input('Введите число 1: '))
b = int(input('Введите число 2: '))
c = str(input('Введите знак (+, -, *, /, **): '))
if c=='+':
    print(a+b)
elif c=='-':
    print(a-b)
elif c == '*':
    print(a * b)
elif c=='/':
        print(a/b)
elif c=='**':
    print(a**b)