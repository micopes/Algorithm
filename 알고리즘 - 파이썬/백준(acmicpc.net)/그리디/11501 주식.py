import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    
    n = int(input().rstrip())
    stock = list(map(int, input().rstrip().split()))
    max_list = [0 for _ in range(n)]
    max_val = 0
    
    ans = 0
    
    for i in range(n-1, -1, -1):
        if max_val < stock[i]:
            max_val = stock[i]
        max_list[i] = max_val
    
    for i in range(n):
        if stock[i] < max_list[i]:
            ans += max_list[i] - stock[i]
    
    print(ans)
            
