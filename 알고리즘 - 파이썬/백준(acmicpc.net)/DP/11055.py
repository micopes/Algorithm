n = int(input())

dp = [0 for _ in range(1000)] # 0 ~ 999

a = list(map(int, input().split()))

# 1. 초기값
for i in range(n):
    dp[i] = a[i]
    
# 2. 점화식
for i in range(n):
    for j in range(i, n):
        if a[i] < a[j]:
            dp[j] = max(dp[i] + a[j], dp[j])

# 3. 결과값
print(max(dp))