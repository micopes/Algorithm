import sys
# input = sys.stdin.readline

n = int(input().rstrip())

numbers = list(map(int, input().rstrip().split()))

m = int(input().rstrip())

dp = [ [0 for _ in range(n)] for __ in range(n)]

for i in range(n):
    dp[i][i] = 1

for i in range(n-1):
    if numbers[i] == numbers[i+1]:
        dp[i][i+1] = 1

for x in range(2, n):
    for i in range(n-x):
        j = i + x
        if dp[i+1][j-1] == 1 and numbers[i] == numbers[j]:
            dp[i][j] = 1
    

for _ in range(m):
    start, end = map(int, input().rstrip().split())
    print(dp[start-1][end-1])