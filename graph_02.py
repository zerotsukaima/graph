n=int(input("Введите число вершин в графе "))

k=int(input("Введите число ребер в графе "))

graphMatrix=[[int(x) for x in input().split()] for i in range(n)]
verOnePower=[]  # вершины, инцидентные только 1-му ребру
Max=0

def vertices(b=False): # по умолчанию False
    global graphMatrix
    global verOnePower
    global Max
    for i in range(n):
        count=0 #количество вершин счетчик степени
        for j in range(k): # и пошли проверять ребра
            if graphMatrix[i][j] != 0: #решаем пункт а в б) и если не равно нулю увеличиваем счетчик на 1
                if b:
                    count+=1
                if not b:
                    print(i, j) #и вывели индексы ребер
        if b:
            if count>Max:
                Max=count
            if count==1:
                verOnePower.append(i) #только одного соседа одно иинцидентное ребро решение для г
            print(i, count) #б) номер вершины и ее степень

def haveZeroPower():
    global graphMatrix
    a=[]
    for i in range(n): #по строчкам матрицы, т.е. по вершинам
        if k==len([x for x in graphMatrix[i] if x==0]):
            #генерируем список, бежим по элементам в строке и если оно равно нулю, мы все их выписываем и в списке из нулей смотрим длину
            a.append(i)#добавляем если элементы и если все элементы ноль
    print('в)В графе нет вершин со степенью ноль') if len(a)==0 else print('в)Вершина(ы) графа со степенью ноль:', *a)
    #параметры собирает в кортеж как join map принцип работы

def haveLoop():
    global graphMatrix
    a=[]
    for i in range(n):
        for j in range(k):
            if graphMatrix[i][j]==2:
                a.append(i)
    print('е)В графе петель не обнаружено') if len(a)==0 else print("е)В графе обнаружено", len(a), "петель в вершинах:", *a)

print('а)Список вершин с инцидентными им ребрами')
vertices()
print('б)Степени вершин графа')
vertices(True)
haveZeroPower()
print('г)Число вершин, инцидентных 1 ребру:', len(verOnePower))
print('д)Максимальное число смежных ребер:', Max)
haveLoop()