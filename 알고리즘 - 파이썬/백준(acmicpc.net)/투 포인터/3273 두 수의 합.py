import sys
# input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))

target = int(input().rstrip())

arr.sort()

i = 0
j = n-1

ans = 0

while i < j:
    sum_val = arr[i] + arr[j]
    
    if sum_val == target:
        ans += 1
        if arr[i] != arr[i+1]:
            i += 1
        if arr[j] != arr[j-1]:
            j -= 1
    elif sum_val > target:
        j -= 1
    elif sum_val < target:
        i += 1
    
print(ans)
        
    
    