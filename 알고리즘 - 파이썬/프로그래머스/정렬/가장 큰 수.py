def solution(numbers):
    answer = ''
    
    num = list(map(str, numbers))
    num.sort(key = lambda x : x*3, reverse = True)
    answer = str(int("".join(num))) # '00' 과 같은 경우 0으로 바꿔주기 위해 int로 바꾼 후 다시 str로 바꿔준다.
    
    return answer