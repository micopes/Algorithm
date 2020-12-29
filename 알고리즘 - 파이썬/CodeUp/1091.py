a, m, d, n = map(int, input().split())

for i in range(n-1):
    a *= m
    a += d

print(a)
    
    