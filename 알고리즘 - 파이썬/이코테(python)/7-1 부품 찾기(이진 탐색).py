import sys
# input = sys.stdin.readline

def binarySearch(array, start, end, target):
    if start > end:
        return False
    mid = (start + end) // 2
    
    if array[mid] == target:
        return True
    elif array[mid] > target:
        end = mid - 1
        return binarySearch(array, start, end, target)
    else:
        start = mid + 1
        return binarySearch(array, start, end, target)
        

n = int(input().rstrip())
nList = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
mList = list(map(int, input().rstrip().split()))

nList.sort()
for x in mList:
    exist = binarySearch(nList, 0, n-1, x)
    if exist == 1:
        print("yes")
    else:
        print("no")


