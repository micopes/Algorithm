# LIS Algorithm
# > 길이는 갱신되어야 LIS가 갱신되는 것이므로, 내부 요소가 바뀌면서 더 좋은 값이 들어가면서 길이를 갱신해야 한다.
import sys
# input = sys.stdin.readline

def binarySearch(start, end, target):
    
    while start <= end:
        mid = (start + end) // 2
        
        if lis[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    
    return start
            
        

n = int(input().rstrip())
nums = list(map(int, input().rstrip().split()))
lis = [0]

for x in nums:
    if lis[-1] < x:
        lis.append(x)
    else:
        lis[binarySearch(0, len(lis)-1, x)] = x

print(len(lis)-1)
    
    