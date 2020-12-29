'''n = int(input())
data = list(map(int, input().split()))

print(min(data))'''

n = int(input())
data = list(map(int, input().split()))
            
result = data[0]

for k in data :
    if k < result :
        result = k

print(result)
    