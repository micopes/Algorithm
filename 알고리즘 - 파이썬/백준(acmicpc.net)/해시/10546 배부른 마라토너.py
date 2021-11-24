import sys
# input = sys.stdin.readline

n = int(input().rstrip())

dic = dict()
for _ in range(n):
    string = input().rstrip()
    if string in dic:
        dic[string] += 1
    else:
        dic[string] = 1

for _ in range(n-1):
    string = input().rstrip()
    dic[string] -= 1

for k in dic.items():
    if k[1] == 1:
        print(k[0])
        break
