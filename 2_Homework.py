#Задача 2937

numb = int(input('Enter the number from 0 to 10000: '))
if numb > 10000:
    print(False)
    numb = int(input('Enter the number from 0 to 10000: '))
if numb < 10000:
    print('The next number for the number ' + str(numb) + ' is ' + str(numb + 1) + '.')
    print('The previous number for the number ' + str(numb) + ' is ' + str(numb


#Задача 3443
import math

print(math.pow(2,179))

#Задача 3445

c = (179**2+971**2) * (0.5)
print(c)

#Задача 3455

a = int(input('Enter the number from 0 to 1000: '))
b = int(input('Enter the number from 0 to 1000: '))
c = round((a**2 + b**2)*(0.5),10)
print (c)

# Задача 3456

name = 'Harry'
print(f'Hello, {name}!')

# Задача 3502

numb1 = int(input('Enter the number: '))
numb2 = int(input('Enter the number: '))
if numb1 > numb2:
    print(numb1)
elif numb2 > numb1:
    print(numb2)

# Задача 3503

numb1 = int(input('Enter the number: '))
if numb1 > 0:
    print(1)
elif numb1 < 0:
    print(-1)
else:
    print(0)

# Задача 3735

my_str = 'Abrakadabra'
print(my_str[2])
print(my_str[-2])
print(my_str[0:5])
print(my_str[0:9])
print(my_str[::2])
print(my_str[1::2])
print(my_str[::-1])
print(my_str[-1::-2])
print(len(my_str))

# Задача 3736

my_str = 'Hello world'
my_str2 = my_str.count(' ') + 1
print(my_str2)

# Задача 111300

simb = str(input('Введите символ: '))
print(ord(simb))

# Задача 111301

num = int(input('Введите число: '))
print(chr(num))


