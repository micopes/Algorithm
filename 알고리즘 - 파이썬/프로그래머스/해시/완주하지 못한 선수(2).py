# 동명이인이 있을 수 있으므로 집합(set)은 사용 불가
# 완주하지 못한 선수는 1명
def solution(participant, completion):
    answer = ''
    
    dic_part = {}
    # 참여 선수
    for x in participant:
        if x in dic_part:
            dic_part[x] += 1
        else:
            dic_part[x] = 1
    # 완주한 경우     
    for x in completion:
        dic_part[x] -= 1
    
    for key, val in dic_part.items():
        if val == 1:
            answer = key
            break
            
    return answer