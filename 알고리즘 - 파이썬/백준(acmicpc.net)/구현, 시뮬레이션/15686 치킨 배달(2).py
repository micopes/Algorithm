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

for ch in combinations(chicken, m):
    temp_ans = 0
    for i in range(len(home)):
        home_x = home[i][0]
        home_y = home[i][1]
        
        temp_ans += min([abs(home_x - j[0]) + abs(home_y - j[1]) for j in ch])
    if ans > temp_ans:
        ans = temp_ans

print(ans)
            
        