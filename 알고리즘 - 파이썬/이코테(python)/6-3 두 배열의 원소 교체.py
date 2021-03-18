import sys
# input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

aList = list(map(int, input().rstrip().split()))
bList = list(map(int, input().rstrip().split()))

aList.sort()
bList.sort(reverse = True)

for i in range(k):
    if aList[i] < bList[i]:
        aList[i] = bList[i]
    
print(sum(aList))
