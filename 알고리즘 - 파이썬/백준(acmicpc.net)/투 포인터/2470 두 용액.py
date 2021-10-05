import sys
input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))

min_val = sys.maxsize
left = 0
right = n-1
answer_left = -1
answer_right = -1

arr.sort()

while left < right:
    sum_val = arr[left] + arr[right]
    
    if min_val > abs(sum_val):
        min_val = abs(sum_val)
        answer_left = left
        answer_right = right
        
    
    if sum_val > 0:
        right -= 1
    elif sum_val < 0:
        left += 1
    else:
        break

print(arr[answer_left], arr[answer_right])
        