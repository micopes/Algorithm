T = int(input())

for l in range(T):
    dp = [[0]*100001 for _ in range(2)] # [2][100000]
    a = [[0]*100001 for _ in range(2)] # [2][100000]
    n = int(input())
    for i in range(2):
        a[i] = list(map(int, input().split()))

    dp[0][0] = a[0][0]
    dp[1][0] = a[1][0]
    
    dp[0][1] = dp[1][0] + a[0][1]
    dp[1][1] = dp[0][0] + a[1][1]
 
    for i in range(2, n):
        dp[0][i] = max( (dp[1][i-1]+a[0][i]), (dp[1][i-2]+a[0][i]) )
        dp[1][i] = max( (dp[0][i-1]+a[1][i]), (dp[0][i-2]+a[1][i]) )
        
    result = max(dp[0][n-1], dp[1][n-1])
    print(result)
    