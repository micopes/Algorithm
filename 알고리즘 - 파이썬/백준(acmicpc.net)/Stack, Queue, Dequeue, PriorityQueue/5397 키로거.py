import sys
from collections import deque
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    left = deque()
    right = deque()
    
    string = input().rstrip()
    cursor = 0
    
    for c in string:
        if c == '<' :
            if left:
                right.appendleft(left.pop())
        elif c == '>':
            if right:
                left.append(right.popleft())
        elif c == '-':
            if left:
                left.pop()
        else:
            left.append(c)
    left.extend(right)
    print("".join(left))
    
