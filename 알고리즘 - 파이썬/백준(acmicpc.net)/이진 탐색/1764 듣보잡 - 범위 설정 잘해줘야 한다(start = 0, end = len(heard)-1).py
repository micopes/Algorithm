import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)

def binarySearch(heard, start, end, x):
    global result
    if start > end:
        return False
    mid = (start + end) // 2
    if x == heard[mid]:
        result.append(x)
        return True
    elif x > heard[mid]:
        return binarySearch(heard, mid+1, end, x)
    else:
        return binarySearch(heard, start, mid-1, x)    

heard = []
n, m = map(int, input().split())

for i in range(n):
    string = input().strip()
    heard.append(string)

heard.sort()

result = []

for i in range(m):
    string = input().strip()
    binarySearch(heard, 0, len(heard)-1, string)

result.sort()
print(len(result))
for val in result:
    print(val)
