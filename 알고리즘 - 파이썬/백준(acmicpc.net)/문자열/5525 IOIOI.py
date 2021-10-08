import sys
# input = sys.stdin.readline

n = int(input().rstrip())
m = int(input().rstrip())
S = input().rstrip()

i = 1
pattern = 0
cnt = 0
while i < m - 1:
    if S[i-1] == 'I' and S[i] == 'O' and S[i+1] == 'I':
        pattern += 1
        if pattern == n:
            cnt += 1
            pattern -= 1
        i += 2
    else:
        pattern = 0
        i += 1

print(cnt)
    