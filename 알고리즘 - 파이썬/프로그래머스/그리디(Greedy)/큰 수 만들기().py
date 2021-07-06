def solution(number, k):
    answer = ''
    
    stack = []
    stack.append(number[0])
    
    for x in number[1:]:
        while len(stack) > 0 and stack[-1] < x and k > 0:
            k -= 1
            stack.pop()
        stack.append(x)
    
    answer = "".join(stack)
    if k != 0:
        answer = answer[:-k]
    
    return answer