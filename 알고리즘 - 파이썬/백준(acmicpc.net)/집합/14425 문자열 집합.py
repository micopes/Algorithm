import sys
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

S = set()
for _ in range(n):
    string = input().rstrip()
    S.add(string)
    
ans = 0
for _ in range(m):
    string = input().rstrip()
    if string in S:
        ans += 1

print(ans)
    