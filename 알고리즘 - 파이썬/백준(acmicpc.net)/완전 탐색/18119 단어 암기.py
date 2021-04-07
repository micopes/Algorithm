import sys
input = sys.stdin.readline

n, m = map(int, input().rstrip().split())

li = [[] for _ in range(26)]
forgot = [0]*n

for i in range(n):
    string = set(input().rstrip())
    for x in string:
        li[ord(x)-ord('a')].append(i)

cnt = n
for _ in range(m):
    command, char = input().rstrip().split()
    if char in ['a', 'e', 'i', 'o', 'u']:
        continue
    if command == '1':
        num = ord(char)-ord('a')
        for i in li[num]:
            if forgot[i] == 0:
                cnt -= 1
            forgot[i] += 1
    else:
        num = ord(char)-ord('a')
        for i in li[num]:
            forgot[i] -= 1
            if forgot[i] == 0:
                cnt += 1
    print(cnt)
            
            
            
        