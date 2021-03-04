import sys
# input = sys.stdin.readline

ans = []
def backtrack(n):
    if n > 9876543210:
        return
    ans.append(n)
    
    last = n % 10
    for i in range(10):
        if last <= i:
            break
        else:
            string = str(n) + str(i)
            backtrack(int(string))
    
n = int(input().rstrip())
for i in range(10): # 0 ~ 9까지 넣어서.
    backtrack(i)

ans.sort()

try:
    print(ans[n])
except:
    print(-1)