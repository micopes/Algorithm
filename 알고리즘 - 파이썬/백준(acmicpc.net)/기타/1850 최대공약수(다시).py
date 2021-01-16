def gcd(a, b):
    while(b):
        t = a % b
        a = b
        b = t
    return a

a, b = map(int, input().split())

res = gcd(a, b)
while(res):
    res -= 1
    print(1, end = "")

