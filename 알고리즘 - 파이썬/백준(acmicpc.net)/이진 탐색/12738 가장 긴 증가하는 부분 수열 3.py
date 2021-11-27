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
lis = [-1000000001]

for x in nums:
    if lis[-1] < x:
        lis.append(x)
    else:
        lis[binarySearch(0, len(lis)-1, x)] = x

print(len(lis)-1)