import sys
from collections import defaultdict
# input = sys.stdin.readline

n, m = map(int, input().rstrip().split())


dic = defaultdict(list)

for i in range(n):
    gg_name = input().rstrip()
    gg_num = int(input().rstrip())
    for j in range(gg_num):
        gg_member = input().rstrip()
        dic[gg_member] = gg_name
        dic[gg_name].append(gg_member)
    
for i in range(m):
    key = input().rstrip()
    num = int(input().rstrip())
    if num == 1:
        print(dic[key])
    else:
        mem_list = list(dic[key])
        mem_list.sort()
        for mem in mem_list:
            print(mem)