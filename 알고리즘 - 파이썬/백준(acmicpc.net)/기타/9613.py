def gcd(a, b):
    while(b):
        t = a % b
        a = b
        b = t
    return a

T = int(input())

for k in range(T):
    result = 0
    data = list(map(int, input().split()))
    data.remove(data[0])
    for i in range(len(data)):
        for j in range(i+1, len(data)):
            result += gcd(data[i], data[j])
    print(result)
            
            

    