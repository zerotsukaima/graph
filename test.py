def add_edge(mat, a, b):
    mat[a][b] = 1

M = int(input('Введите число ребер: '))
K = int(input('Введите число вершин: '))
print('Введите связи между вершинами графа:')
mat = []
verNoEdge = []
Max = 0

for i in range(K):
    mat.append([])
    for j in range(K):
        mat[i].append(0)
for i in range(M):
    a, b = input().split()
    a = int(a)
    b = int(b)
    add_edge(mat, a, b)
    add_edge(mat, b, a)

G = mat
for i in range(len(G)):
    print("")
    for j in range(len(G)):
        print(G[i][j], end=" ")

def loops():
    global G
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j and G[i][j] == 1:
                print('В графе есть петли ')
                return G
    print('В графе нет петель ')

def verZero():
    global G
    global K
    for i in range(K):
        countZeros = 0
        for j in range(K):
            if G[i][j] == 0:
                countZeros += 1
        if countZeros == len(G):
            print('В графе есть вершины, не смежные с другими')
            break
        if i == len(G) - 1:
            print('В графе нет вершин, не смежных с другими')

def verAll():
    global G
    global K
    for i in range(K):
        countOnes = 0
        for j in range(K):
            if G[i][j] == 1:
                countOnes += 1
        if countOnes == len(G):
            print('В графе есть смежные со всеми вершины')
            break
        if i == len(G) - 1:
            print('В графе нет смежных со всеми вершин')

def degreeGraph():
    global G
    global K
    countDegree = 0
    for i in range(K):
        for j in range(K):
            if G[i][j] == 1:
                countDegree += 1
        print(i, countDegree)
        countDegree = 0

def degreeOne():
    global G
    global K
    countDegree = 0
    for i in range(K):
        for j in range(K):
            if G[i][j] == 1:
                countDegree += 1
        if countDegree == 1:
            print(i)
        countDegree = 0

def maxDegree():
    global G
    global K
    global Max
    countDegree = 0
    for i in range(K):
        for j in range(K):
            if G[i][j] == 1:
                countDegree += 1
        if countDegree > Max:
            Max = countDegree
        countDegree = 0
    print(Max)

print('\nа) есть ли в графе петли? ')
loops()
print('\nб) есть ли в графе вершины не смежные с другими?')
verZero()
print('\nг) есть ли в графе вершины смежные со всеми другими вершинами?')
verAll()
print('\nд) вершины и ее степень:')
degreeGraph()
print('\nе) номера вершин со степенью 1:')
degreeOne()
print('\nж) максимальная степень графа:')
maxDegree()
