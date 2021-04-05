import sys
# input = sys.stdin.readline

INF = sys.maxsize

T = int(input().rstrip())
for _ in range(T):
    N, M, W = map(int, input().rstrip().split())
    
    graph = [[INF]*(N+1) for _ in range(N+1)]
    
    for i in range(N+1):
        graph[i][i] = 0
    
    for i in range(M): # 도로 정보
        S, E, T = map(int, input().rstrip().split())
        # 저장된게 새로 생긴 도로보다 길면 짧게 줄인다.
        if graph[S][E] > T :
            graph[S][E] = T
        elif graph[E][S] > T:
            graph[E][S] = T
    
    for i in range(W):
        S, E, T = map(int, input().rstrip().split())
        # S : 시작, E : 도착 도로와 다름.
        if graph[S][E] > -T:
            graph[S][E] = -T
    
    for k in range(N+1):
        for i in range(N+1):
            for j in range(N+1):
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])
                
                
    flag = False
    for i in range(N+1):
        if graph[i][i] < 0:
            flag = True
            break
        
    if flag == True:
        print("YES")
    else:
        print("NO")
        
        
        
    
        
        