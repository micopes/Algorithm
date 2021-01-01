n = int(input())

# 1. 초기값
dp = [1 for _ in range(1000)] # 0 ~ 999

a = list(map(int, input().split()))

# 2. 증감식
for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j]:
            dp[j] = max(dp[i]+1, dp[j])
        
# 3. 결과값
print(max(dp))