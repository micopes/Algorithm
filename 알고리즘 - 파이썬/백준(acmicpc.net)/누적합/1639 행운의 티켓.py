import sys
# input = sys.stdin.readline

S = input().rstrip()
n = len(S)

ans = 0
for i in range(n-1):
    for j in range(i+1, n):
        # 2N자리가 아니면 -> 다음으로
        if (j-i+1) % 2 != 0:
            continue

        l = (j-i+1)//2
        temp1, temp2 = 0, 0
        for k in range(i, i+l):
            temp1 += int(S[k])
        
        for k in range(j-l+1, j+1):
            temp2 += int(S[k])
        
        if temp1 == temp2:
            ans = max(ans, 2*l)
            

print(ans)
            
            
            