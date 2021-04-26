import sys
# input = sys.stdin.readline

string = input().split('-')
ans = 0
for i in string[0].split('+'):
    ans += int(i)
for i in range(1, len(string)):
    temp = 0
    k = string[i].split('+')
    for j in k:
        temp += int(j)
    ans -= temp
print(ans)
        
    