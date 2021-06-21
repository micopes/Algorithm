def solution(clothes):
    type = dict()
    for k in clothes:
        try:
            type[k[1]] += 1
        except:
            type[k[1]] = 1
    
    ret = 1
    for i in type:
        ret *= (type[i]+1) # 0개 입는 것 포함
    
    ret -= 1 # 하나의 의상도 입지 않을 경우
    return ret