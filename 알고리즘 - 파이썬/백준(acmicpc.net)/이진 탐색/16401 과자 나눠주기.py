import sys
# input = sys.stdin.readline
m, n = map(int, input().rstrip().split())

arr = list(map(int, input().rstrip().split()))

start = 0
end = max(arr)
ans = 0
while start <= end:
    poss_num = 0
    mid = (start + end) // 2
    # divide by zero 대비
    if mid == 0:
        break
    
    for x in arr:
        if x >= mid:
            poss_num += x//mid
    
    if poss_num >= m:
        start = mid + 1
        ans = mid
    else:
        end = mid - 1
    
print(ans)