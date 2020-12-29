def gcd(a, b):
    while(b != 0) :
        r = a % b
        a = b
        b = r
    return a

def lcm(a, b) :
    return a * b / gcd(a, b)

a, b, c = map(int, input().split())

result = lcm(lcm(a, b), c)
result = int(result)
print(result)

        