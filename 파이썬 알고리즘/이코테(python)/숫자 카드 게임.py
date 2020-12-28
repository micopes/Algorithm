result = 0

n, m = map(int, input().split())

for i in range(n) :
    data = list(map(int, input().split()))
    value = min(data)
    result = max(result, value)
    
print(result)