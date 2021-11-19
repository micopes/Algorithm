import sys
# input = sys.stdin.readline

n, k = int(input().rstrip()), int(input().rstrip())

start = 1
end = k

ans = 0
while start <= end:
    mid = (start + end) // 2
    
    temp = 0
    for i in range(1, n+1):
        temp += min(n, mid//i)
    
    if temp >= k:
        ans = mid
        end = mid - 1
    else:
        start = mid + 1

print(ans)