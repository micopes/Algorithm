import sys
input = sys.stdin.readline

_ucpc = ['U', 'C', 'P', 'C']

string = input().strip()

index = 0
for i in range(len(string)):
    if index == 4:
        break
    if _ucpc[index] == string[i]:
        index += 1

if index == 4:
    print("I love UCPC")
else:
    print("I hate UCPC")
        
    
