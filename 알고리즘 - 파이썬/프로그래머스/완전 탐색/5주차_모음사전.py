from itertools import product
def solution(word):
    answer = 0
        
    ans_list = []
    mo = ['A', 'E', 'I', 'O', 'U']

    for i in range(1, 6): # 1 ~ 5
        for k in product(mo, repeat = i):
            temp = "".join(k)
            ans_list.append(temp)

    ans_list.sort()
    for i in range(len(ans_list)):
        # i+1
        if ans_list[i] == word:
            answer = i+1

    return answer

