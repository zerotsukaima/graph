n = int(input('Введите число вершин в графе: '))
k = int(input('Введите число ребер в графе: '))

graph = [[int(x) for x in input().split()] for i in range(n)]

graph_matrix = []
loop = []
level = []
counter = 0
counter_0 = 0
counter_not_0 = 0
maxx = 0

for i in range(n):
    graph_matrix.append([])
    for j in range(n):
        graph_matrix[i].append(0)

def node():
    for i in graph:
        if len(i) == 2:
            a, b = i[0], i[1]
            matrix(a, b)
            matrix(b, a)

def matrix(a, b):
    for i in range(n):
        if i == a:
            for j in range(n):
                if j == b:
                    graph_matrix[i][j] = 1
node()

print('\nМатрица смежности')
for i in range(n):
    print('')
    for j in range(n):
        print(graph_matrix[i][j], end=' ')
print('\n')

for i in range(n):
    print('Вершина ' + str(i) + ' смежна с вершинами: ', end=' ')
    for j in range(n):
        if i == j and graph_matrix[i][j] == 1:
            loop.append(i)
        if graph_matrix[i][j] == 1:
            print(j, end=' ')
    print('')

for i in range(n):
    for j in range(n):
        if graph_matrix[i][j] == 1:
            counter += 1
            if counter == n:
                print('\nВершина смежная со всеми вершинам:', i)
                print('')
        if graph_matrix[i][j] == 0:
            counter_0 += 1
            if counter_0 == n:
                print('\nВершина не смежная с другими:', i)
                print('')
            if counter_0 < n:
                counter_not_0 += 1
    counter_0 = 0
    counter = 0

for i in range(n):
    print('Степень вершины ' + str(i) + ' - ', end='')
    for j in range(n):
        if graph_matrix[i][j] == 1:
            counter += 1
    print(counter)
    if counter == 1:
        level.append(i)
    if counter > maxx:
        maxx = counter
    counter = 0

if counter_not_0 == n:
    print('\nВ графе нет вершин не смежных со другими.')

if len(loop) > 0:
    print('\nВершины с петлями:', *loop)
else:
    print('\nВ графе нет врешин с петлями.')

if maxx < n:
    print('\nВ графе нет вершин смежных со всеми вершинами.')

if len(level) > 0:
    print('\nВершины со степенью 1:', *level)
else:
    print('\nВ графе нет врешин со степенью 1.')

print('\nСтепень графа:', maxx)