import sys
input = sys.stdin.readline
sys.setrecursionlimit(111111)
INF = sys.maxsize
def dist(a, b):
    return (a[0]-b[0])**2 + (a[1]-b[1])**2

def divConq(start, end):
    if start == end:
        return INF
    elif end - start == 1:
        return dist(arr[end], arr[start])
    mid = (start + end) // 2
    temp = min(divConq(start, mid), divConq(mid+1, end))
    
    cand = []
    for i in range(start, end + 1):
        if (arr[mid][0] - arr[i][0])**2 < temp:
            cand.append(arr[i])
    cand.sort(key = lambda x : x[1])
    
    for i in range(len(cand)-1):
        for j in range(i+1, len(cand)):
            dy = (cand[i][1] - cand[j][1]) ** 2
            if dy < temp:
                temp = min(temp, dist(cand[i], cand[j]))
            else:
                break
    return temp
            

n = int(input().strip())
arr = []
for i in range(n):
    x, y = map(int, input().strip().split())
    arr.append([x, y])

arr.sort()

print(divConq(0, len(arr)-1))

    