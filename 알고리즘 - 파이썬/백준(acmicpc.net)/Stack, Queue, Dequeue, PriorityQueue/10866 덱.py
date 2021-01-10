import sys
from collections import deque
input = sys.stdin.readline
d = deque()
n = int(input())

for i in range(n):
    string = input().split()
    if string[0] == 'push_front':
        d.appendleft(string[1])
    elif string[0] == 'push_back':
        d.append(string[1])
    elif string[0] == 'pop_front':
        if len(d) == 0:
            print(-1)
        else:
            print(d.popleft())
    elif string[0] == 'pop_back':
        if len(d) == 0:
            print(-1)
        else:
            print(d.pop())
    elif string[0] == 'size':
        print(len(d))                   
    elif string[0] == 'empty':
        if len(d) == 0:
            print(1)
        else:
            print(0)
    elif string[0] == 'front':
        if len(d) == 0:
            print(-1)
        else:
            print(d[0])
    elif string[0] == 'back':
        if len(d) == 0:
            print(-1)
        else:
            print(d[-1])
            