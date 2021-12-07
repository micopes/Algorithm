import sys
import math

input = sys.stdin.readline

def solve(n):
	for i in range(2, int(math.sqrt(n))+1):
		if n % i == 0:
			return False
	return True

n = int(input().rstrip())
print(solve(n))

	