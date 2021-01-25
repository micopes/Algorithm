import sys
# input = sys.stdin.readline

n = int(input().strip())

maxScore = 0
_list = []
for i in range(n):
    name, score = input().strip().split()
    score = int(score)
    _list.append([name, score])
    maxScore = max(maxScore, score)

cand = []
for i in range(n):
    if _list[i][1] == maxScore:
        cand.append(_list[i][0])

cand.sort()
print(cand[0])
    
    