import sys
# input = sys.stdin.readline

DIV = 1000000007

def init(idx, start, end):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    
    mid = (start + end) // 2
    
    temp = init(idx*2, start, mid) * init(idx*2+1, mid+1, end) % DIV
    tree[idx] = temp
    return temp

def update(idx, start, end, i, val):
    if i < start or end < i:
        return 
    
    if start == end:
        tree[idx] = val
        return tree[idx]
    
    mid = (start + end) // 2
    
    if i <= mid:
        update(idx*2, start, mid, i, val)
    else:
        update(idx*2+1, mid+1, end, i, val)
        
    tree[idx] = tree[idx*2] * tree[idx*2+1] % DIV

def getSum(idx, start, end, left, right):
    if end < left or right < start:
        return 1
    
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    return getSum(idx*2, start, mid, left, right) * getSum(idx*2+1, mid+1, end, left, right) % DIV



n, m, k = map(int, input().rstrip().split())

arr = []

for i in range(n):
    num = int(input().rstrip())
    arr.append(num)

tree = [0]*(n*4)
init(1, 0, n-1)

for i in range(m+k):
    a, b, c = map(int, input().rstrip().split())
    if a == 1:
        arr[b-1] = c
        update(1, 0, n-1, b-1, c)
    elif a == 2:
        print(getSum(1, 0, n-1, b-1, c-1))
        