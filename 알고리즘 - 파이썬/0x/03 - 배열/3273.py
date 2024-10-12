import sys
from collections import defaultdict
input = sys.stdin.readline

n = int(input().rstrip())
val_list = list(map(int, input().split()))
x = int(input().rstrip())

val_list.sort()

cnt = 0
left = 0
right = n-1

while left < right:
	sum_val = val_list[left] + val_list[right]
	
	if sum_val == x:
		cnt += 1
		
		# 중복 값 제거 위해
		left += 1
		right -= 1
	elif sum_val < x:
		left += 1
	elif sum_val > x:
		right -= 1

print(cnt)
		
	
	
