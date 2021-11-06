import sys
from collections import deque
input = sys.stdin.readline

a, b, c, d = map(int, input().rstrip().split())

visited = {}
visited[(0, 0)] = 1

q = deque()
q.append((0, 0))

flag = False
while q:
    x, y = q.popleft()
    if c == 0 and d == 0:
        flag = True
        print(0)
        break
    
    # Fill A
    if not visited.get((a, y)):
        q.append((a, y))
        visited[(a, y)] = visited[(x, y)] + 1
    
    # Fill B
    if not visited.get((x, b)):
        q.append((x, b))
        visited[(x, b)] = visited[(x, y)] + 1

    # Empty A
    if not visited.get((0, y)):
        q.append((0, y))
        visited[(0, y)] = visited[(x, y)] + 1
    
    # Empty B
    if not visited.get((x, 0)):
        q.append((x, 0))
        visited[(x, 0)] = visited[(x, y)] + 1
    
    # A -> B
    if x + y < b:
        if not visited.get((0, x+y)):
            q.append((0, x+y))
            visited[(0, x+y)] = visited[(x, y)] + 1
    else:
        if not visited.get((x+y-b, b)):
            q.append((x+y-b, b))
            visited[(x+y-b, b)] = visited[(x, y)] + 1
            
    # B -> A
    if x + y < a:
        if not visited.get((x+y, 0)):
            q.append((x+y, 0))
            visited[(x+y, 0)] = visited[(x, y)] + 1
    else:
        if not visited.get((a, x+y-a)):
            q.append((a, x+y-a))
            visited[(a, x+y-a)] = visited[(x, y)] + 1
        
    if visited.get((c, d)):
        ans = visited[(x, y)]
        print(ans)
        flag = True
        break

if flag == False:
    print(-1)
