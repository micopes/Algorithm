def solution(citations):
    answer = 0
    
    citations.sort(reverse = True)
    
    for i in range(len(citations)):
        if citations[i] > answer:
            answer += 1 # h
        else:
            break
    
    return answer