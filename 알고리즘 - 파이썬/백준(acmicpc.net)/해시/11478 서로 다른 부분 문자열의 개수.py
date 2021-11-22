import sys
input = sys.stdin.readline

string = input().rstrip()
n = len(string)

string_set = set()
for length in range(1, n+1):
    idx = 0
    while idx < n:
        string_set.add(string[idx:idx+length])
        idx += 1
        
print(len(string_set))
    
    