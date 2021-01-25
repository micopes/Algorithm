import sys
input = sys.stdin.readline

n, k = map(int, input().strip().split())

coin = []
for i in range(n):
    x = int(input().strip())
    coin.append(x)

coin.reverse()

coinNum = 0
for i in range(n):
    coinNum += k // coin[i]
    k = k % coin[i]

print(coinNum)
    