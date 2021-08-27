def solution(s):
    answer = len(s)
    
    for step in range(1, len(s)//2 + 1):
        compressed = ""
        prev = s[0:step]
        cnt = 1
        
        for j in range(step, len(s), step):
            # 이전의 문자와 같은 경우
            if prev == s[j:j+step]:
                cnt += 1
            # 이전의 문자와 다른 경우
            else:
                if cnt == 1:
                    compressed += prev
                else:
                    compressed += str(cnt)
                    compressed += prev
                prev = s[j:j+step]
                cnt = 1
        
        if cnt == 1:
            compressed += prev
        else:
            compressed += str(cnt)
            compressed += prev
            
        answer = min(answer, len(compressed))
    
    return answer

# s = "aagrajgoejgriae"
# print(s[10:30]) 는 print(s[10:20])과 같다. 넘어가면 그 이상은 없는 것으로 처리된다.