import sys
input = sys.stdin.readline

visited = [0 for _ in range(31)]

for i in range(28):
    x = int(input().rstrip())
    visited[x] = 1

for i in range(1, 31):
    if visited[i] == 0:
        print(i)
    