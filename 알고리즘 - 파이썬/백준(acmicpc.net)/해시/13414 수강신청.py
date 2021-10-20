import sys
# input = sys.stdin.readline

K, L = map(int, input().rstrip().split())

dic = {}
for i in range(L):
    number = input().rstrip()
    dic[number] = i
    
li = []
for key, item in dic.items():
    li.append([item, key])

li.sort()

cnt = 0
for x in li:
    print(x[1])
    
    cnt += 1
    if cnt == K:
        break
    
    
    