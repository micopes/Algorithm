n = int(input())

a = list(map(int, input().split()))

dp1 = [1 for _ in range(1000)] 
dp2 = [1 for _ in range(1000)]

for i in range(n):
    for j in range(i+1, n):
        if a[i] < a[j] and dp1[j] < dp1[i] + 1:
            dp1[j] = dp1[i] + 1

for i in range(n-1, -1, -1):
    for j in range(i-1, -1, -1):
        if a[i] < a[j] and dp2[j] < dp2[i] + 1:
            dp2[j] = dp2[i] + 1

result = 0
for i in range(n):
    result = max(result, dp1[i] + dp2[i])

print(result-1) # 중간에 있는 것은 2번 사용되기 때문에 -1
