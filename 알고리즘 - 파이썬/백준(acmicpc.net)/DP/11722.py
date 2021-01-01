# 1. 초기값
dp = [1 for _ in range(1000)]

n = int(input())

data = list(map(int, input().split()))

# 2. 점화식
for i in range(n):
    for j in range(i+1, n):
        if data[i] > data[j]:
            dp[j] = max(dp[i]+1, dp[j])
            
# 3. 결과값
print(max(dp))
            