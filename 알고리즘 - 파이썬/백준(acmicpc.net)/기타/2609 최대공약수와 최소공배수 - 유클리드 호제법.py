def gcd(a, b):
    while b:
        t = a % b
        a = b
        b = t
    return a

a, b = map(int, input().split())
print(gcd(a, b))
print((a*b)//gcd(a, b))