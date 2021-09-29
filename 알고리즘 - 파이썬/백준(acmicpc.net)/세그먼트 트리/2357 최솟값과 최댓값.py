import sys
input = sys.stdin.readline

def init(idx, start, end):
    if start == end:
        tree[idx] = [arr[start], arr[end]]
        return tree[idx]
    
    mid = (start + end) // 2
    
    temp1, temp2 = init(idx*2, start, mid), init(idx*2+1, mid+1, end)
    min1, max1 = temp1[0], temp1[1]
    min2, max2 = temp2[0], temp2[1]
    
    tree[idx] = [min(min1, min2), max(max1, max2)]
    return tree[idx]

def get_minmax(idx, start, end, left, right):
    if end < left or right < start:
        return [1000000000, -1000000000]
    
    if left <= start and end <= right:
        return tree[idx]
    
    mid = (start + end) // 2
    temp1 = get_minmax(idx*2, start, mid, left, right)
    temp2 = get_minmax(idx*2+1, mid+1, end, left, right)
    min1, max1 = temp1[0], temp1[1]
    min2, max2 = temp2[0], temp2[1]
    
    return [min(min1, min2), max(max1, max2)]

n, m = map(int, input().rstrip().split())

arr = []
for i in range(n):
    num = int(input().rstrip())
    arr.append(num)

tree = [[0, 0] for _ in range(n*4)]
init(1, 0, n-1)

for i in range(m):
    # 번째임에 주의 a-1 ~ b-1까지 구해야 한다.
    a, b = map(int, input().rstrip().split())
    temp = get_minmax(1, 0, n-1, a-1, b-1)
    print(temp[0], temp[1])
    
    

