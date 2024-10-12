import sys
from collections import defaultdict
input = sys.stdin.readline

# 6, 9는 더해서 2로 나눈 값을 올림
s = str(input().rstrip())

dic = defaultdict(int)
for c in s:
	dic[int(c)] += 1

if (dic[6] + dic[9]) % 2 == 0:
	dic[6] = (dic[6] + dic[9]) // 2
	dic[9] = 0
else:
	dic[6] = (dic[6] + dic[9]) // 2 + 1
	dic[9] = 0
	
print(max(dic.values()))

