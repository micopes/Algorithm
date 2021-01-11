n = int(input())

result = []
while n > 1:
    if n % 2 == 0:
        result.append(2)
        n = n // 2
    else:
        for i in range(3, n+1, 2): # 2 ~ n
            if n % i == 0:
                result.append(i)
                n = n // i
                break
  
        
result.sort()
for i in range(len(result)):
    print(result[i])
        
        