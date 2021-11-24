import sys
# input = sys.stdin.readline

A_num, B_num = map(int, input().rstrip().split())
A_set = set(map(int, input().rstrip().split()))
B_set = set(map(int, input().rstrip().split()))

ans_set = A_set - B_set
print(len(ans_set))

ans_list = list(ans_set)
ans_list.sort()
for x in ans_list:
    print(x, end = " ")