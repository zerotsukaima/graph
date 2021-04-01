n=int(input("Введите число вершин в графе"))

k=int(input("Введите число ребер в графе"))
graphMatrix=[[int(x) for x in input().split()] for i in range(n)]
verOnePower=[]  # вершины, инцидентные только 1-му ребру
Max=0
def vertices(b=False):
    global graphMatrix
    global verOnePower
    global Max
    global haveLoop
    for i in range(n):
        count=0
        for j in range(k):
            if graphMatrix[i][j] != 0:
                if b:
                    count+=1
                if not b:
                    print(i, j)
        if b:
            if count>Max:
                Max=count
            if count==1:
                verOnePower.append(i)
            print(i, count)
def haveZeroPower():
    global graphMatrix
    a=[]
    for i in range(n):
        if k==len([x for x in graphMatrix[i] if x==0]):
            a.append(i)
    print('в)В графе нет вершин со степенью ноль') if len(a)==0 else print('в)Вершина(ы) графа со степенью ноль:', *a)
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