import sys
# input = sys.stdin.readline

n = int(input().rstrip())

arr = list(map(int, input().rstrip().split()))

arr.sort()

min_val = sys.maxsize


answer_left = -1
answer_right = -1


# 두 포인터가 O(N)이므로 시간복잡도 O(N^2)
for i in range(n):
    mid = i
    start = 0
    end = n-1
    
    flag = False # 조기에 0인 것을 발견한 경우
    while start < mid and mid < end:
        sum_val = arr[start] + arr[mid] + arr[end]
        
        if min_val > abs(sum_val):
            min_val = abs(sum_val)
            answer_start = start
            answer_mid = mid
            answer_end = end
        
        if sum_val > 0:
            end -= 1
        elif sum_val < 0:
            start += 1
        else:
            flag = True
            break
    if flag == True:
        break

print(arr[answer_start], arr[answer_mid], arr[answer_end])
            