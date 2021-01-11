n = int(input())

# 0! = 1, 1! = 1
result = 1
for i in range(1, n+1):
    result *= i
    
print(result)