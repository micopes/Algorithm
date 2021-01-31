import sys
from collections import deque
# input = sys.stdin.readline

T = int(input().strip())

for t in range(T):
    scores = list(map(int, input().strip().split()))
    scores.sort()
    scores = deque(scores)
    scoreSum = scores.popleft() + scores.pop()
    if scores[-1] - scores[0] >= 4:
        print("KIN")
    else:
        print(sum(scores))
        
    
    