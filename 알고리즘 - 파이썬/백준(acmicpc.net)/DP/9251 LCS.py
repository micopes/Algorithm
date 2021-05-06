import sys
# input = sys.stdin.readline

string1 = input().rstrip()
string2 = input().rstrip()

length1 = len(string1)
length2 = len(string2)

dp = [[0]*(length2+1) for _ in range(length1+1)]

for i in range(1, length1+1):
    for j in range(1, length2+1):
        if string1[i-1] == string2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

print(dp[-1][-1])

    
                
        



