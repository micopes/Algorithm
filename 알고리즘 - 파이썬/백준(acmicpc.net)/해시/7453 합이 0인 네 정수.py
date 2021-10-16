import sys
input = sys.stdin.readline

n = int(input())
A, B, C, D = [], [], [], []
answer = 0

for _ in range(n):
    a, b, c, d = map(int, input().rstrip().split())
    A.append(a)
    B.append(b)
    C.append(c)
    D.append(d)
    

hash_table = {}
for a in A:
    for b in B:
        if not hash_table.get(a+b):
            hash_table[a+b] = 1
        else:
            hash_table[a+b] += 1

for c in C:
    for d in D:
        try:
            answer += hash_table[-(c+d)]
        except:
            continue

print(answer)
