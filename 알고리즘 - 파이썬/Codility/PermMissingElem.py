def solution(A):
    n = len(A)
    visited = [0 for i in range(n+2)] # 1 ~ n+1까지의 index 중 0인 값.

    for x in A:
        visited[x] = 1
    
    for i in range(1, n+2):
        if visited[i] == 0:
            return i

