import sys
# input = sys.stdin.readline

def isPoss(string):
    mo = 0
    za = 0
    for ch in string:
        if ch in 'aeiou':
            mo += 1
        else:
            za += 1
        if mo >= 1 and za >= 2:
            ans.add(''.join(sorted(string)))

def backtrack(string, idx):
    if len(string) == L:
        isPoss(string)
        return
    for i in range(idx, C):
        if visited[i] == 0:
            visited[i] = 1
            string += data[i]
            backtrack(string, i)
            visited[i] = 0
            string = string[:-1]

L, C = map(int, input().rstrip().split())
data = list(input().rstrip().split())
visited = [0 for _ in range(26)]
ans = set()
string = ""
idx = 0

backtrack(string, idx)
ans = sorted(list(ans))
for i in ans:
    print(i)