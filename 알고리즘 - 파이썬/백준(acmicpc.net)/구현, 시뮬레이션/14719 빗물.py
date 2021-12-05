import sys
# input = sys.stdin.readline

h, w = map(int, input().rstrip().split())
graph = list(map(int, input().rstrip().split()))

ans = 0
for i in range(1, w-1):
    left = max(graph[:i])
    right = max(graph[i+1:])
    
    m = min(left, right)
    
    if m > graph[i]:
        ans += m - graph[i] 
print(ans)
    