from collections import deque

init = list(input())
n = int(input())

left = deque(init)
right = deque()

for i in range(n):
    command = input().split()
    if command[0] == 'L':
        if len(left) != 0:
            right.appendleft(left.pop())
    if command[0] == 'D':
        if len(right) != 0:
            left.append(right.popleft())
    if command[0] == 'B':
        if len(left) != 0:
            left.pop()
    if command[0] == 'P':
        left.append(command[1])

result = left + right

for i in result:
    print(i, end = "")