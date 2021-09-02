def solution(A):
    number = {}

    for x in A:
        try:
            number[x] += 1
        except:
            number[x] = 1
    
    for val in A:
        if number[val] % 2 == 1:
            return val
