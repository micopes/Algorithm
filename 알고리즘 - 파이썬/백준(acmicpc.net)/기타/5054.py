import sys
input = sys.stdin.readline

T = int(input().rstrip())
for _ in range(T):
    n = int(input().rstrip())
    shop = list(map(int, input().rstrip().split()))
    print((max(shop)-min(shop))*2)