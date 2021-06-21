def solution(participant, completion):
    answer = ''
    
    parti = dict()
    comple = dict()
    
    for i in participant:
        try:
            parti[i] += 1
        except:
            parti[i] = 0
    for i in completion:
        try:
            comple[i] += 1
        except:
            comple[i] = 0
    
    for i in set(participant):
        try:
            parti[i] -= comple[i]
            if parti[i] == 1:
                answer = i
        except:
            answer = i

    return answer