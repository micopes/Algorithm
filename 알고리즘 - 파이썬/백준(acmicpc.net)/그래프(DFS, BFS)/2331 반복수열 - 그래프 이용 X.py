a, p = map(int, input().split())

visited = [0 for _ in range(1000001)]
visited[a] = 1
for i in range(100000):
    k = 0
    while a:
        temp = a % 10
        k += temp ** p
        a //= 10
    visited[k] += 1
    a = k
    
count = 0
for i in range(1000001):
    if visited[i] == 1:
        count += 1
        
print(count)