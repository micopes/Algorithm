import sys
# input = sys.stdin.readline

n = int(input().rstrip())
arr = list(map(int, input().rstrip().split()))

arr.sort()
# 찾고자 하는 수
ans = 0
for i in range(n):
    left = 0
    right = n-1
    val = arr[i]
    
    while left < right:
        tmp = arr[left] + arr[right]
        
        if tmp == val:
            if left != i and right != i:
                ans += 1     
                break
            # arr[a]라는 수가 arr[b]와 arr[c]의 합으로 되어야 '좋다'.
            elif left == i:
                left += 1
            else:
                right -= 1
        elif tmp > val:
            right -= 1
        else:
            left += 1
            
print(ans) 
