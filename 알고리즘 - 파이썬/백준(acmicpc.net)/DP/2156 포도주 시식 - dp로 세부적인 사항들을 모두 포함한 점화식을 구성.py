drink = [0 for _ in range(10001)] # 0 ~ n-1
dp = [0 for _ in range(10001)]

# 입력
n = int(input())

for i in range(n):
    drink[i] = int(input())

# 초기값
dp[0] = drink[0]
dp[1] = dp[0] + drink[1]

for i in range(2, n):
    dp[i] = max(dp[i-1], dp[i-3]+drink[i-1]+drink[i], dp[i-2]+drink[i])

print(dp[n-1])