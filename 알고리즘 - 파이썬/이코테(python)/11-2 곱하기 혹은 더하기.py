s = input()

data = [0 for _ in range(20)]

for i in range(len(s)):
    data[i] = int(s[i])
    
result = data[0]    
for i in range(1, len(s)):
    result = max(result*data[i], result+data[i])
    
print(result)