a = int(input('Введите первое число '))
b = int(input('Введите второе число '))
c = int(input('Введите третье число '))
d = int(input('Введите четвертое число '))
e = int(input('Введите пятое число '))

if a < b and a < c and a < d and a < e:
    print (f'Min {a}')
elif b < a and b < c and b < d and b < e:
    print (f'Min {b}')
elif c < a and c < b and c < d and c < e:
    print (f'Min {c}')
elif d < a and d < b and d < c and d < e:
    print (f'Min {d}')
elif e < a and e < b and e < c and e < d:
        print (f'Min {e}')

