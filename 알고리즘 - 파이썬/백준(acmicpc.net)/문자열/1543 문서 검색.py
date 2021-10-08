import sys
input = sys.stdin.readline

string = input()
word = input()
idx = 0

cnt = 0
while idx <= len(string) - len(word):
    if string[idx:idx+len(word)] == word:
        cnt += 1
        idx = idx + len(word)
    else:
        idx += 1
        
print(cnt)
        
    