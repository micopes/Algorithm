import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

num_list = []
for i in range(n):
    x = int(input().rstrip())
    num_list.append(x)

num_list.sort()
left, right = 0, 0
ans = sys.maxsize

while left <= right and right < n:
    tmp = num_list[right] - num_list[left]
    
    if tmp == m:
        ans = m
        break
    elif tmp < m:
        right += 1
    else:
        left += 1
        ans = min(ans, tmp)
    
print(ans)
