import sys
# input = sys.stdin.readline

def solve(n):
    print(n, end = " ")
    if n == 1:
        return
    if n % 6 == 0:
        if dp[n//3] <= dp[n//2] and dp[n//3] <= dp[n-1]:
            solve(n//3)
            return
        elif dp[n//2] <= dp[n//3] and dp[n//2] < dp[n-1]:
            solve(n//2)
            return
        else:
            solve(n-1)
    elif n % 3 == 0:
        if dp[n//3] <= dp[n-1]:
            solve(n//3)
            return
        else:
            solve(n-1)
            return
    elif n % 2 == 0:
        if dp[n//2] <= dp[n-1]:
            solve(n//2)
            return
        else:
            solve(n-1)
            return
    else:
        solve(n-1)    

dp = [0 for _ in range(1000001)]

n = int(input().rstrip())

dp[1] = 0
dp[2] = 1
dp[3] = 1

for i in range(4, n+1):
    dp[i] = sys.maxsize
    if i % 3 == 0:
        temp = dp[i//3] + 1
        dp[i] = min(dp[i], temp)
    if i % 2 == 0:
        temp = dp[i//2] + 1
        dp[i] = min(dp[i], temp) 
    temp = dp[i-1] + 1
    dp[i] = min(dp[i], temp)

print(dp[n])
solve(n)


    


    

