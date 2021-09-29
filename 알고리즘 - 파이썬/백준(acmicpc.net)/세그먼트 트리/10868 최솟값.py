import sys
# input = sys.stdin.readline

def init(idx, start, end):
    if start == end:
        tree[idx] = arr[start]
        return tree[idx]
        
    mid = (start + end) // 2
    
    tree[idx] = min(init(idx*2, start, mid), init(idx*2+1, mid+1, end))
    return tree[idx]

def get_min(idx, start, end, left, right):
    if end < left or right < start:
        return 1000000000
    
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    
    return min(get_min(idx*2, start, mid, left, right), get_min(idx*2+1, mid+1, end, left, right))


n, m = map(int, input().rstrip().split())

arr = []
for i in range(n):
    num = int(input().rstrip())
    arr.append(num)

tree = [0]*(n*4)

init(1, 0, n-1)

for i in range(m):
    a, b = map(int, input().rstrip().split())
    print(get_min(1, 0, n-1, a-1, b-1))
    