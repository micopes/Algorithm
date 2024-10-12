import sys
from collections import defaultdict
input = sys.stdin.readline

s = input().rstrip()

dic = defaultdict(int)
for c in s:
	dic[ord(c)-ord('a')] += 1

for idx in range(ord('z') - ord('a') + 1):
	print(dic[idx], end = " ")
