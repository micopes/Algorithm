import sys
# input = sys.stdin.readline

n = int(input().rstrip())
data = list(map(int, input().rstrip().split()))

dic = {}
val = 0
temp = sorted(data)
dic[temp[0]] = 0
val += 1
for i in range(1, len(temp)):
    if temp[i] == temp[i-1]:
        continue
    dic[temp[i]] = val
    val += 1

for i in data:
    print(dic[i], end = " ")
    
    
    
    
    
    