
def solution(n, times):
    ans = -1
    times.sort()
    min_t = times[0]
    max_t = times[0]*n
    
    while True:
        mid = (min_t + max_t) // 2
        cnt = 0
        for x in times:
            cnt += mid // x
        
        if cnt >= n:
            max_t = mid
        else:
            min_t = mid
        
        if min_t == (max_t-1): # 나머지 1이 되는 경우
            ans = max_t
            break
    
    
    return ans
