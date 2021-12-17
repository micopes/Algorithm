import sys
# input = sys.stdin.readline

n = int(input().rstrip())

distance = list(map(int, input().rstrip().split()))

cost = list(map(int, input().rstrip().split()))

min_cost = cost[0]

ans = 0

for i in range(len(distance)):
    min_cost = min(min_cost, cost[i])
    
    ans += distance[i]*min_cost
    
print(ans)