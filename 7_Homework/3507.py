#Задача №3507. Сколько совпадает чисел
#Даны три целых числа. Определите, сколько среди них совпадающих.
# Программа должна вывести одно из чисел: 3 (если все совпадают), 2 (если два совпадает) или 0 (если все числа различны).

a = 12
b = 12
c = 14

if a==b==c:
    print(3)
elif a==b or b==c or a==c:
    print(2)
else:
    print(0)