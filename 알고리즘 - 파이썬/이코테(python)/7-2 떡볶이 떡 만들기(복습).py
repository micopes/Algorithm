import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

dduk = list(map(int, input().rstrip().split()))
result = []

start = 0
end = max(dduk)

while start <= end:
    total = 0
    mid = (start + end) // 2
    
    for x in dduk:
        if x > mid:
            total += x - mid
    
    if total < m:
        end = mid - 1
    else:
        start = mid + 1
        result.append(mid)

print(max(result))