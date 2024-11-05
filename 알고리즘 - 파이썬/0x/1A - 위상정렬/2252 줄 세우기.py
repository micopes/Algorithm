import sys
input = sys.stdin.readline
from collections import deque

n, m = map(int, input().split())

indegree = [0 for _ in range(n+1)] # 찔리는 쪽
graph = [[] for _ in range(n+1)] # 찌르는쪽

# 찔리는 쪽이 0이면 순서에 추가하면 되며, 추가할 때 찌르는 쪽의 indegree를 감소시키면 된다. - 모르겠으면 바킹독 유튜브 강의 참고 재학습
for i in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    indegree[b] += 1

q = deque()
for i in range(1, n+1):
    if indegree[i] == 0:
        q.append(i)

while q:
    a = q.popleft()
    print(a, end = " ")
    for b in graph[a]:
        indegree[b] -= 1
        if indegree[b] == 0:
            q.append(b)



