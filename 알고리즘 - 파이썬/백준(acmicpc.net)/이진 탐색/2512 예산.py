import sys
# input = sys.stdin.readline

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
total = int(input().rstrip())

start, end = 0, max(nums)

while start <= end:
    mid = (start + end) // 2
    temp_total = 0
    
    for num in nums:
        if num > mid:
            temp_total += mid
        else:
            temp_total += num
    
    if temp_total > total:
        end = mid - 1
    else:
        start = mid + 1

print(end)
        
            