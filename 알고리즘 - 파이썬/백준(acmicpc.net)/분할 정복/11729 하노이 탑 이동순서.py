import sys
# input = sys.stdin.readline
sys.setrecursionlimit(111111)

_list = []
def hanoi_tower(start, temp, end, n):
    if n == 1:
        _list.append([start, end])
    else:
        hanoi_tower(start, end, temp, n-1)
        _list.append([start, end])
        hanoi_tower(temp, start, end, n-1)
    
n = int(input().strip())

hanoi_tower(1, 2, 3, n)
print(len(_list))
for i in range(len(_list)):
    print("%d %d" % (_list[i][0], _list[i][1]))
