import sys
input = sys.stdin.readline

alpha = [0 for _ in range(26)]

n = int(input().rstrip())


for i in range(n):
    string = input().rstrip()
    idx = ord(string[0]) - ord('a')
    alpha[idx] += 1
    
ans_list = []
for i in range(len(alpha)):
    if alpha[i] >= 5:
        ans_list.append(chr(ord('a') + i))
    
if len(ans_list) == 0:
    print("PREDAJA")
else:
    ans_list.sort()
    for x in ans_list:
        print(x, end = "")

    