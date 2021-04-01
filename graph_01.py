#построение матрицы смежности для графа

def read_graph():
    M = N = int(input())
    G = []
    for i in range(M):
        G.append([])
        for j in range(N):
            G[i].append(input().split())
    return G

def add_edge(G, a, b, weight):
    if a not in G:
        G[a] = []
    G[a][b] = weightв

G = read_graph()
print(G)