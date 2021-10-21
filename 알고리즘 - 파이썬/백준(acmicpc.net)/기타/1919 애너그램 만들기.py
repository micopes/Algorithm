import sys
# input = sys.stdin.readline

str1 = list(input().rstrip())
str2 = list(input().rstrip())

str1_list = [0 for _ in range(26)]
str2_list = [0 for _ in range(26)]

for x in str1:
    str1_list[ord(x) - ord('a')] += 1

for x in str2:
    str2_list[ord(x) - ord('a')] += 1

ans = 0
for i in range(26):
    x = str1_list[i]
    y = str2_list[i]
    
    ans += abs(x-y)
    
print(ans)
    
    