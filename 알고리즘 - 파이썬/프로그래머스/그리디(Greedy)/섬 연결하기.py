def find(parent, n):
    if n == parent[n]:
        return n
    
    parent[n] = find(parent, parent[n])
    return parent[n]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    
    if a == b:
        return a
    
    if a < b:
        parent[b] = a
    else:
        parent[a] = b
    
    return -1

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)]
    cnt = 0
    
    costs.sort(key = lambda x : x[2])
    
    for x in costs:
        a, b, w = x[0], x[1], x[2]
        # 연결되어 있지 않은 경우
        if union(parent, a, b) == -1:
            answer += w
            cnt += 1
        if cnt == n-1:
            break
    return answer