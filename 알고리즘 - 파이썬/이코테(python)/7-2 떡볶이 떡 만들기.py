import sys
# input = sys.stdin.readline

def binarySearch(array, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    
    global ans
    val = 0
    for x in array:
        # 자를 높이 이상이어야만 짜를 수 있다.
        if x > mid:
            val += (x - mid)
    
    if val == target:
        return mid
    elif val > target:
        '''
        if ans < val:
            ans = val
        '''
        start = mid + 1
        return binarySearch(array, start, end, target)
    else:
        '''
        if ans < val:
            ans = val
        '''
        end = mid - 1
        return binarySearch(array, start, end, target)
        
            
    

# 개수 n, 길이 m
n, m = map(int, input().rstrip().split())
array = list(map(int, input().rstrip().split()))
ans = 0
print(binarySearch(array, min(array), max(array), m))
