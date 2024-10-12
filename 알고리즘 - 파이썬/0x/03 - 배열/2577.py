import sys
from collections import defaultdict
input = sys.stdin.readline

A = int(input().rstrip())
B = int(input().rstrip())
C = int(input().rstrip())

res = A * B * C

str_res = str(res)
dic = defaultdict(int) # int의 default값은 0.
for c in str_res:
	dic[int(c)] += 1 
	
for i in range(10):
	print(dic[i])
	
