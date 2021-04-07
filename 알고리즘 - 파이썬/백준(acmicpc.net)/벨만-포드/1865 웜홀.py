import sys
input = sys.stdin.readline
INF = sys.maxsize

def bf(start):
    dist = [INF]*(v+1)
    dist[start] = 0
    
    for i in range(v):
        for edge in edges: # 매번 모든 간선을 체크.
            cur = edge[0]
            next_v = edge[1]
            cost = edge[2] 
            
            if dist[next_v] > dist[cur] + cost:
                dist[next_v] = dist[cur] + cost
                if i == v-1:
                    return True
                
    return False
    

T = int(input().rstrip())
for _ in range(T):
    v, e, w = map(int, input().rstrip().split())
    edges = []

    for _ in range(e):
        x, y, d = map(int, input().rstrip().split())
        edges.append((x, y, d))
        edges.append((y, x, d))
        
    for _ in range(w):
        s, e, t = map(int, input().rstrip().split())
        edges.append((s, e, -t))
    
    negative_cycle = bf(1)
    if negative_cycle:
        print("YES")
    else:
        print("NO")
        
    
    
        
        