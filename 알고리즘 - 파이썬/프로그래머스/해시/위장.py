def solution(clothes):
    answer = 0
    dic = {}
    wearname = []
    for i in range(len(clothes)):
        try:
            dic[clothes[i][1]] += 1
        except:
            dic[clothes[i][1]] = 1
            wearname.append(clothes[i][1])
    
    answer = 1
    for i in range(len(wearname)):
        answer *= (dic[wearname[i]]+1)
    answer -= 1
    
    return answer