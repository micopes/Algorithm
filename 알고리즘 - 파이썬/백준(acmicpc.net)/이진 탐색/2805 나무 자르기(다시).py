import sys
input = sys.stdin.readline

n, m = map(int, input().split())

tree = list(map(int, input().strip().split()))

start, end = 0, 1000000000

while start <= end:
    mid = (start + end) // 2
    
    height = 0
    for k in tree:
        if k >= mid:
            height += k - mid
    
    if height >= m:
        start = mid + 1
    else:
        end = mid - 1

print(end)
        
    