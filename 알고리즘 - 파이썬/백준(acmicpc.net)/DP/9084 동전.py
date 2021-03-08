import sys
# input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    N = int(input().rstrip())
    coin = list(map(int, input().rstrip().split()))
    M = int(input().rstrip())
    
    dp = [0 for _ in range(M+1)]
    dp[0] = 1
    
    for i in range(N):
        for j in range(coin[i], M+1):
            dp[j] += dp[j-coin[i]]
        
    print(dp[M])
        
        
    
    