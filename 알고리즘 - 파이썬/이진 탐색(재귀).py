def binarySearch(array, start, end, target):
    if start > end:
        return None
    mid = (start + end) // 2
    
    if array[mid] == target:
        return mid
    elif array[mid] > target:
        return binarySearch(array, start, mid-1, target)
    else:
        return binarySearch(array, mid+1, end, target)
    
    
n, target = list(map(int, input().rstrip().split()))
array = list(map(int, input().rstrip().split()))

result = binarySearch(array, 0, n-1, target)
if result == None:
    print("원소가 존재하지 않습니다")
else:
    print(result + 1)
        