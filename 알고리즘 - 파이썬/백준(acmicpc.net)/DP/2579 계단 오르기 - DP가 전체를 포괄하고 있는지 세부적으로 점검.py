# 밟은 계단의 개수를 저장할 수 있어야 함.

n = int(input())

a = [0 for _ in range(300)]
for i in range(n):
    x = int(input())
    a[i] = x
    
dp = [[0]*3 for _ in range(300)] # [299][2]

# 초기값
dp[0][1] = a[0] # 한개 연속
dp[0][2] = a[0] # 2개 연속 -> ?

dp[1][1] = a[1]
dp[1][2] = a[0] + a[1]

# 점화식
for i in range(2, n):
    dp[i][1] = max(dp[i-2][2], dp[i-2][1]) + a[i]
    dp[i][2] = dp[i-1][1] + a[i]


# 결과값
result = max(dp[n-1][1], dp[n-1][2])
print(result)