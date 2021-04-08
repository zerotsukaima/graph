x = int(input('Введите число от 1 до 9: '))

if x <= 3 and x >= 1:
    s = str(input('Введите строку '))
    n = int(input('ВВедите число повторов строк '))
    for i in range(n):
        print(s)
elif x <= 6 and x >= 4:
    m = int(input('Введите степень, в которую надо возвести число '))
    x = x ** m
    print(x)
elif x <= 9 and x >= 7:
    for i in range(10):
        x += 1
        print(x)
else:
    print('Error!!!')
