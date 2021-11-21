import sys
# input = sys.stdin.readline

dic = {}

n = int(input().rstrip())
max_val = 0
for i in range(n):
    book = input().rstrip()
    try:
        dic[book] += 1
        max_val = max(dic[book], max_val)
    except:
        dic[book] = 0
        
ans_list = []
for x in dic.keys():
    if dic[x] == max_val:
        ans_list.append(x)

ans_list.sort()
print(ans_list[0])
