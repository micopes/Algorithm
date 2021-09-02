def solution(X, Y, D):
    ans = 0
    if (Y-X) % D == 0:
        ans = (Y-X) // D
    else:
        ans = (Y-X) // D + 1
    
    return ans