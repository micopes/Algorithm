def solution(v):
    answer = []

    x_dic = {}
    y_dic = {}

    for x, y in v:
        if x in x_dic:
            x_dic[x] += 1
        else:
            x_dic[x] = 1
        
        if y in y_dic:
            y_dic[y] += 1
        else:
            y_dic[y] = 1
    
    for key, val in x_dic.items():
        if val == 1:
            answer.append(key)
            
    for key, val in y_dic.items():
        if val == 1:
            answer.append(key)
    
    
    return answer