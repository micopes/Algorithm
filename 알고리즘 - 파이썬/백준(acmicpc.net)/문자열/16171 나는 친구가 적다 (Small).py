import sys
input = sys.stdin.readline


def solve(S, K):
    idx = 0
    while idx <= len(S) - len(K):
        if S[idx:idx + len(K)] == K:
            return 1
        else:
            idx += 1
    
    return 0
    
S = list(input().rstrip())
real_S = []

K = input().rstrip()

for i in range(len(S)):
    if not '0' <= S[i] <= '9':
        real_S.append(S[i])

S = "".join(real_S)

print(solve(S, K))
        
        
    

