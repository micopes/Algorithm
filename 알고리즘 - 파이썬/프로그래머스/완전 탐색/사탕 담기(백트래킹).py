cnt = 0
def recur(m, weights, temp_list, idx):
    global cnt
    if sum(temp_list) + weights[idx] == m:
        cnt += 1
    elif sum(temp_list) > m:
        return
    
    if idx+1 < len(weights):
        # 현재 idx 넣지 않는다
        recur(m, weights, temp_list, idx+1)
        
        # 현재 idx 넣는다. -> 이후에 제거(pop)
        temp_list.append(weights[idx])
        recur(m, weights, temp_list, idx+1)
        temp_list.pop()
        
def solution(m, weights):
    answer = 0
    recur(m, weights, [], 0)
    
    return cnt