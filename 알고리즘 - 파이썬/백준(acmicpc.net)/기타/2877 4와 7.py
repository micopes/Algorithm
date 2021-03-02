import sys
input = sys.stdin.readline

K = int(input().rstrip())
K += 1
b = bin(K)

ans = b[2::]
ans = list(ans)

for i in range(1, len(ans)):
    if ans[i] == '0':
        ans[i] = '4'
    else:
        ans[i] = '7'


ans = "".join(ans)
ans = ans[1::]
print(ans)