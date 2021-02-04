from collections import deque
import sys
input = sys.stdin.readline

def cou(s1, s2):
    if visited[s1][s2] != 1:
        visited[s1][s2] = 1
        q.append([s1, s2])
        
def bfs():
    
    while q:
        a1, b1 = q.popleft()
        c1 = c-a1-b1
        
        if a1 == 0:
            result.append(c1)
        
        if a1 + b1 < b: # a -> b
            cou(0, a1+b1)
        else:
            cou(a1-(b-b1), b)
            
        if a1 + c1 < c: # a -> c
            cou(0, b1)
        else:
            cou(a1-(c-c1), b1)
        
        if b1 + c1 < c: # b -> c
            cou(a1, 0)
        else:
            cou(a1, b1-(c-c1))
        
        if b1 + a1 < a: # b -> a
            cou(b1+a1, 0)
        else:
            cou(a, b1-(a-a1))
        
        if c1 + a1 < a: # c -> a
            cou(c1+a1, b1)
        else:
            cou(a, b1)
        
        if c1 + b1 < b: # c -> b
            cou(a1, c1+b1)
        else:
            cou(a1, b)
            
a, b, c = map(int, input().rstrip().split())
visited = [[0]*201 for _ in range(201)]
result = []
q = deque()

cou(0, 0)
bfs()
result.sort()

print(' '.join(map(str, result)))
