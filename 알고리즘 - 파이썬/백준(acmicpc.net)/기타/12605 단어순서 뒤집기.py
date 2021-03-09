import sys
# input = sys.stdin.readline

n = int(input().rstrip())

string = []
for i in range(n):
    temp = list(input().rstrip().split())
    temp = temp[::-1]
    string.append(temp)
    
for i in range(1, n+1):
    print("Case #%d:" % i, end = " ")
    temp = " ".join(string[i-1])
    print(temp)