n, b = input().split()
n = list(n)
b = int(b)

res = []
while n:
    if n[0] >= '0' and n[0] <= '9':
        res.append(int(n[0]))
    else:
        res.append(ord(n[0]) - ord('A') + 10)
    n.remove(n[0])
    
res.reverse()

result = 0
for i in range(len(res)):
    result += (res[i]*(b**i))
print(result)


