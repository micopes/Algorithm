import sys
input = sys.stdin.readline

n = int(input().strip())
m = int(input().strip())
broken = list(input().strip().split())

result = sys.maxsize
val = ""
for i in range(0, 1000000):
    string = str(i)
    flag = True
    for j in range(len(string)):
        if string[j] in broken:
            flag = False
            
    result = min(result, abs(100-n))
    if flag == True:
        result = min(result, (len(string) + abs(int(string) - n)))
                    
print(result)
            
            
    