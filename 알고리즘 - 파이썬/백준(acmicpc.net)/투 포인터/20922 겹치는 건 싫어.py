import sys
# input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
count_list = [0 for _ in range(max(arr)+1)]

left, right = 0, 0
ans = 0

while left <= right and right < n:
    if count_list[arr[right]] < k:
        count_list[arr[right]] += 1
        right += 1
    else:
        count_list[arr[left]] -= 1
        left += 1
    
    ans = max(ans, right - left)

print(ans)