import sys
# input = sys.stdin.readline

def init(idx, start, end):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
    
    mid = (start + end) // 2
    tree[idx] = init(idx*2, start, mid) + init(idx*2+1, mid+1, end)
    return tree[idx]

def update(idx, start, end, i, diff):
    tree[idx] += diff
    
    if start == end:
        return

    mid = (start + end) // 2
    if i <= mid:
        update(idx*2, start, mid, i, diff)
    else:
        update(idx*2+1, mid+1, end, i, diff)

def interval_sum(idx, start, end, left, right):
    if left > end or right < start:
        return 0
    
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    
    return interval_sum(idx*2, start, mid, left, right) + interval_sum(idx*2+1, mid+1, end, left, right)


N, M, K = map(int, input().rstrip().split())

arr = []

for i in range(N):
    num = int(input())
    arr.append(num)

tree = [0]*(N*4)

init(1, 0, N-1)

for i in range(M + K):
    a, b, c = map(int, input().rstrip().split())
    if a == 1:
        diff = c - arr[b-1]
        arr[b-1] = c
        update(1, 0, N-1, b-1, diff)
    elif a == 2:
        print(interval_sum(1, 0, N-1, b-1, c-1))