def add_edge(mat, a, b):
    mat[a][b] = 1

M = int(input('Введите число ребер: '))
K = int(input('Введите число вершин: '))
mat = []

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
    global K
    global M
    for i in range(len(G)):
        for j in range(len(G)):
            if i == j and G[i][j] == 1:
                print('\n\nВ графе есть петли ')
                return G
    print('\n\nВ графе нет петель ')

loops()

