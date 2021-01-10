def gcd(a, b):
    while(b):
        t = a % b
        a = b
        b = t
    return a

def lcm(a, b):
    return a*b//gcd(a, b)

# main
n = int(input())
for i in range(n):
    a, b = map(int, input().split())
    print(lcm(a, b))
    
