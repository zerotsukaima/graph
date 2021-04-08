x = int(input("Введите число от 1 до 9: "))
if 3 >= x >= 1:
    s = input("Введите строку: ")
    n = int(input("Введите количество повторов строки: "))
    for i in range(n):
        print(s)
elif 6 >= x >= 4:
    m = int(input("Введите степень в которую возвести число: "))
    print(x ** m)
elif 9 >= x >= 7:
    for i in range(0, 10):
        x += 1
        print(x)
else:
    print("Ошибка ввода")