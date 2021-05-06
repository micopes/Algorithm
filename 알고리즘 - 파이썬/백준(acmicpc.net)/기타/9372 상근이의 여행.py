import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n, m = map(int, input().rstrip().split())
    for i in range(m):
    	x, y = map(int, input().rstrip().split())
    print(n-1)