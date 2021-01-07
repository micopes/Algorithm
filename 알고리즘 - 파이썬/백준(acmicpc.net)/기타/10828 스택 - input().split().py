import sys

input = sys.stdin.readline

n = int(input())
st = []

for i in range(n):
    string = input().split()
    if string[0] == 'push':
        st.append(string[1])
    if string[0] == 'pop':
        if len(st) == 0:
            print(-1)
        else:
            print(st.pop())
    if string[0] == 'size':
        print(len(st))
    if string[0] == 'empty':
        if len(st) == 0:
            print(1)
        else:
            print(0)
    if string[0] == 'top':
        if len(st) == 0:
            print(-1)
        else:
            print(st[-1])