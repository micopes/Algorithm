from itertools import combinations
import sys

# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

city = []

for i in range(n):
    city.append(list(map(int, input().rstrip().split())))
    

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
ans = sys.maxsize

for k in combinations(chicken, m):
    chicken = []
    temp_ans = 0
    for ch in k:
        chicken.append(ch)
    
    for i in range(len(home)):
        home_x = home[i][0]
        home_y = home[i][1]
        dist = sys.maxsize
        for j in range(len(chicken)):
            chicken_x = chicken[j][0]
            chicken_y = chicken[j][1]
            temp = abs(home_x - chicken_x) + abs(home_y - chicken_y)
            if dist > temp:
                dist = temp
        # print(dist)
        temp_ans += dist
        
    if temp_ans < ans:
        ans = temp_ans

print(ans)
        
# %%

from itertools import combinations
import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

city = []

for i in range(n):
    city.append(list(map(int, input().rstrip().split())))

home = []
chicken = []

for i in range(n):
    for j in range(n):
        if city[i][j] == 1:
            home.append([i, j])
        elif city[i][j] == 2:
            chicken.append([i, j])
            
            
ans = sys.maxsize

for ch in combinations(chicken, m):
    temp_ans = 0
    for i in range(len(home)):
        home_x = home[i][0]
        home_y = home[i][1]
        
        temp_ans += min([abs(home_x - j[0]) + abs(home_y - j[1]) for j in ch])
    if ans > temp_ans:
        ans = temp_ans

print(ans)
            
        