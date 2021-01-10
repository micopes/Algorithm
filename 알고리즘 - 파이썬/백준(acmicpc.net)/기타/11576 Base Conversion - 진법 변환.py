# A, B진법 2이상 30이하.
A, B = map(int, input().split())
n = int(input())
data = list(map(int, input().split()))

res = 0
data.reverse()
for i in range(len(data)): # A -> 10진법
    res += data[i]*(A**i)

result = []
while res:
    result.append(res % B)
    res = res // B
    

result.reverse()
for i in range(len(result)):
    print(result[i], end = " ")


    
