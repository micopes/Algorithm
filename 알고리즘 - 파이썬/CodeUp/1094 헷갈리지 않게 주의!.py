n = int(input())
data = list(map(int, input().split()))

for i in range(n-1, -1, -1):
    print(data[i], end = " ")