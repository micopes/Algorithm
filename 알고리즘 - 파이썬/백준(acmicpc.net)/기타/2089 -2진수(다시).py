n = int(input())
flag = False
if n == 0:
    flag = True
n = n * -1
res = []

while abs(n) >= 0.25:
    k = n % 2
    
    res.append(-k)
    n //= -2

res.reverse()

for i in range(len(res)):
    res[i] *= -1
    print(res[i], end = "")
if flag:
    print(0)
    
'''
n = int(input())
minus = 1
ans = ''
if n == 0:
    ans = '0'
while n:
    if n % 2 == 1:
        ans += '1'
        if minus:
            n -= 1
        else:
            n += 1
    else:
        ans += '0'
    n //= 2
    minus = 1 - minus

print(ans[::-1])
'''