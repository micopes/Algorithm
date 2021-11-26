import sys
# input = sys.stdin.readline

n = int(input().rstrip())

dic = {}

for _ in range(n):
    a, b = input().rstrip().split('.')
    if b not in dic:
        dic[b] = 1
    else:
        dic[b] += 1

ans_list = list(dic.items())
ans_list.sort()

for a, b in ans_list:
    print(a, b)
    