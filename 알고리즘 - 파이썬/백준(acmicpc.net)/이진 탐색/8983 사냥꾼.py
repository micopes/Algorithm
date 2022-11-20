import sys
from bisect import bisect_left
input = sys.stdin.readline
# 사대의 수 m, 동물의 수 n, 사정거리 l
m, n, l = map(int, input().rstrip().split())
sniper = list(map(int, input().rstrip().split()))

sniper.sort()
animal = []
result = 0
for _ in range(n):
	x, y = map(int, input().rstrip().split())
	# 해당 동물에서 가장 가까운 사대의 위치를 찾고 거리가 사격 가능한 거리인지를 확인하면 된다.
	if y <= l:
		idx = bisect_left(sniper, x)
		for k in (idx-1, idx, idx+1):
			if k < 0 or k > len(sniper)-1:
				continue
			dist = abs(sniper[k]-x) + y
			if dist <= l:
				result += 1
				break
		
print(result)
	
