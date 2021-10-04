graph = []

for i in range(2):
    graph.append(list(map(int, input().rstrip().split())))

print(graph)

r = len(graph)
c = len(graph[0])


graph2 = [[0 for _ in range(r)] for _ in range(c)]

for i in range(len(graph)):
    for j in range(len(graph[0])):
        try:
            graph2[j][i] = graph[i][c-j-1]
        except:
            print(i, j)
        

print(graph2)