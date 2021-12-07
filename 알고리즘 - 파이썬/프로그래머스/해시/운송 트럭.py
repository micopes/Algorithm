def solution(max_weight, specs, names):
    dic = {}
    for key, val in specs:
        dic[key] = int(val)
    
    cnt = 1 # truck count
    temp_weight = max_weight
    for key in names:
        w = dic[key]
        if temp_weight < w:
            cnt += 1
            temp_weight = max_weight - w
        else:
            temp_weight -= w
    
    return cnt