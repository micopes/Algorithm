import sys
# input = sys.stdin.readline

def dfs(idx):
    global curSum, cnt
    if idx == n:
        return
    
    if curSum + data[idx] == s:
        cnt += 1
    
    # 현재의 것 포함 x
    dfs(idx+1)
    
    # 현재의 것 포함 o
    curSum += data[idx]
    dfs(idx+1)
    
    curSum -= data[idx]

n, s = map(int, input().rstrip().split())
data = list(map(int, input().rstrip().split()))

idx, curSum = 0, 0
cnt = 0
dfs(idx)
print(cnt)
