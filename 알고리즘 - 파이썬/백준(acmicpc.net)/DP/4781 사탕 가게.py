# int(float(m)*100 + 0.5) 0.5를 더해줌으로써 실수 부동소수점 오차 방지
# 여러 번 들어갈 수 있는 사탕.

import sys
# input = sys.stdin.readline

while True:
    n, m = input().rstrip().split()
    if n == "0" and m == "0.00":
        break
    n, m = int(n), int(float(m)*100+0.5)
    
    
    dp = [0 for _ in range(m+1)]
    for _ in range(n):
        c, p = input().rstrip().split()
        c, p = int(c), int(float(p)*100+0.5)
        for i in range(p, m+1):
            dp[i] = max(dp[i], dp[i-p] + c)
        
    print(dp[m])    
    