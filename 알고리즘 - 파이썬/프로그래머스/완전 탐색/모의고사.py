def solution(answers):
    ans = []
    num1 = [1, 2, 3, 4, 5]
    num2 = [2, 1, 2, 3, 2, 4, 2, 5]
    num3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    cnt1 = 0
    cnt2 = 0
    cnt3 = 0
    
    
    for i in range(len(answers)):
        if num1[i % 5] == answers[i]:
            cnt1 += 1
        if num2[i % 8] == answers[i]:
            cnt2 += 1
        if num3[i % 10] == answers[i]:
            cnt3 += 1
            
    if cnt1 == max(cnt1, cnt2, cnt3):
        ans.append(1)
    if cnt2 == max(cnt1, cnt2, cnt3):
        ans.append(2)
    if cnt3 == max(cnt1, cnt2, cnt3):
        ans.append(3)

    ans.sort()
    
    return ans