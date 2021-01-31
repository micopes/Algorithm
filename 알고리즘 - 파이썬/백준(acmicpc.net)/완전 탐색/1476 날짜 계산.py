'''
1 <= E <= 15
1 <= S <= 28
1 <= M <= 19
'''
import sys
input = sys.stdin.readline

E, S, M = map(int, input().strip().split())

x, y, z = 0, 0, 0
cnt = 0
for i in range(7980):
    x += 1
    y += 1
    z += 1
    cnt += 1
    if x == 16:
        x = 1
    if y == 29:
        y = 1
    if z == 20:
        z = 1
    
    if x == E and y == S and z == M:
        print(cnt)
        break
    
    


