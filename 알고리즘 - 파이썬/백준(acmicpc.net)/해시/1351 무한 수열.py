import sys
# input = sys.stdin.readline

def dfs(n):
    if n in dp:
        return dp[n]
    
    dp[n] = dfs(n//p) + dfs(n//q)
    return dp[n]


n, p, q = map(int, input().rstrip().split())

dp = {}
dp[0] = 1

print(dfs(n))