import sys
# input = sys.stdin.readline

n, c = map(int, input().rstrip().split())

house = []
for i in range(n):
    x = int(input().rstrip())
    house.append(x)

house.sort()

start = 1
end = house[-1] - house[0]
ans = 0

while start <= end:
    mid = (start + end) // 2
    cnt = 1 # 맨 앞에서 맨 뒤까지 1개 추가하고 시작해야 한다. 나누는 것이므로 개수 +1
    old = house[0]
    
    # house[i]와 house[old]간의 거리가 mid 이상인 것을 하나씩 찾으면서 진행한다.
    for i in range(1, n):
        if house[i] - old >= mid:
            cnt += 1
            old = house[i]
            
    
    # 개수는 충족 => 최소 크기를 늘여서 mid를 늘인다 -> 최대 거리 구한다.
    if cnt >= c:
        start = mid + 1
        ans = mid
    # 개수가 충족되지 않으므로 mid를 줄인다 -> 개수를 충족시킨다.
    else:
        end = mid - 1

print(ans)
    