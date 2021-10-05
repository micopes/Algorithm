import sys
# input = sys.stdin.readline

home = []

n = int(input().rstrip())

for i in range(n):
    home.append(list(map(int, input().rstrip().split())))

ans = sys.maxsize

# dp를 색깔마다 갱신한다.
for i in range(3):
    dp = [ [0 for _ in range(3)] for __ in range(n) ]
    
    dp[0][0] = sys.maxsize
    dp[0][1] = sys.maxsize
    dp[0][2] = sys.maxsize
    # i가 0번째 색칠된 색깔
    dp[0][i] = home[0][i]
    
    for j in range(1, n):
        dp[j][0] = min(dp[j-1][1], dp[j-1][2]) + home[j][0]
        dp[j][1] = min(dp[j-1][0], dp[j-1][2]) + home[j][1]
        dp[j][2] = min(dp[j-1][0], dp[j-1][1]) + home[j][2]
    
    
    temp = sys.maxsize
    for j in range(3):
        if i != j:
            temp = min(dp[n-1][j], temp)
    
    if temp < ans:
        ans = temp
        
print(ans)