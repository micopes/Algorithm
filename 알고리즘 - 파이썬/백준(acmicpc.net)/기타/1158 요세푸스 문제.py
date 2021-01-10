from collections import deque

d = deque()

n, k = map(int, input().split())
for i in range(1, n+1):
    d.append(i)

index = 1
result = []
while len(d) != 0:
    index = index % k
    if index != 0:
        d.append(d.popleft())
    else:
        result.append(d.popleft())
    index += 1

print("<", end = "")
for i in range(len(result)):
    print(result[i], end = "")
    if i != (len(result)-1):
        print(",", end = " ")

print(">", end = "")
        
    



