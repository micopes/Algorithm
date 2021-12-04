import sys
input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
	n, k = map(int, input().rstrip().split())
	graph = []
	for _ in range(n):
		graph.append(list(map(int, input().rstrip().split())))
	
	# 최대. 최솟값으로 갱신하면서 진행한다.
	min_val = n*n
	
	for i in range(n-k+1):
		for j in range(n-k+1):
			temp_cnt = 0
			for a in range(k):
				for b in range(k):
					if graph[i+a][j+b] == 1:
						temp_cnt += 1
			min_val = min(min_val, temp_cnt)
	
	print(min_val)