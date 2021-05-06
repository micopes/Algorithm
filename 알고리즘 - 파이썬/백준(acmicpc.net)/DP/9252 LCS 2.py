import sys
# input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

length1 = len(string1)
length2 = len(string2)

dp = [[""]*(length2+1) for _ in range(length1+1)]

for i in range(1, length1 + 1):
    for j in range(1, length2 + 1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + string1[i-1]
        else: # 여기서 문제 생길 수 있다.
            if len(dp[i-1][j]) > len(dp[i][j-1]):
                dp[i][j] = dp[i-1][j]
            else:
                dp[i][j] = dp[i][j-1]

print(len(dp[-1][-1]))
print(dp[-1][-1])

            
    
            