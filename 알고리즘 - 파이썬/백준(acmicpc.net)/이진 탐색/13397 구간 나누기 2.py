import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())
data = list(map(int, input().rstrip().split()))

left = 0
right = 10000

while left <= right:
    mid = (left + right) // 2
    cnt = 1
    max_val = min_val = data[0]
    
    for i in range(n):
        if min_val > data[i]:
            min_val = data[i]
        if max_val < data[i]:
            max_val = data[i]
        if max_val - min_val > mid: # 이 지점에서 max_val - min_val이 mid를 넘으면 1개 더 만듬.
            min_val = data[i]
            max_val = data[i]
            cnt += 1

    if cnt > m: # 원하는 개수보다 많으면 다음 mid의 임계값을 높여서 m에 맞게 만들어준다.
        left = mid + 1
    else:
        right = mid - 1
        
print(left)
        
        