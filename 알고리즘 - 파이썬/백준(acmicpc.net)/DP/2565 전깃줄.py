import sys
# input = sys.stdin.readline

n = int(input().rstrip())

pole = []
dp = [1]*n
for i in range(n):
    a, b = map(int, input().rstrip().split())
    pole.append((a, b))
    
pole.sort()

for i in range(n):
    for j in range(i):
        if pole[j][1] < pole[i][1]:
            dp[i] = max(dp[i], dp[j]+1)

# 전체 전깃줄 - 제대로 증가하는 것의 개수 = 교차하는 전깃줄
ans = n - max(dp)
print(ans)
    
        