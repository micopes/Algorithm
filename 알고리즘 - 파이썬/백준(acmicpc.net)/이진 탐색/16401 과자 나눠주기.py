import sys

# 조카의 수, 과자의 수
m, n = map(int, sys.stdin.readline().split())
# 과자의 길이
arr = list(map(int, sys.stdin.readline().split()))

start = 0
end = max(arr)

result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    # 모든 조카에게 같은 길이의 막대과자를 나눠줄 수 없을 때
    if mid == 0:
        total = 0
        break
    
    for x in arr:
        if x >= mid:
            total += (x//mid)

    if total >= m:
        start = mid + 1
        result = mid
        
    else:
        end = mid - 1

print(result)