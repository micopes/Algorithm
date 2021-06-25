import sys
# input = sys.stdin.readline

def binarySearch(start, end, x):
    mid = (start + end) // 2
    if start > end:
        return False
    
    if store[mid] == x:
        return True
    elif store[mid] > x:
        end = mid-1
        return binarySearch(start, end, x)
    else:
        start = mid+1
        return binarySearch(start, end, x)
    

n = int(input().rstrip())
store = list(map(int, input().rstrip().split()))

m = int(input().rstrip())
buyer = list(map(int, input().rstrip().split()))


store.sort()
start = 0
end = len(store)-1
for i in range(m):
    if binarySearch(start, end, buyer[i]) == True:
        print("yes", end = " ")
    else:
        print("no", end = " ")