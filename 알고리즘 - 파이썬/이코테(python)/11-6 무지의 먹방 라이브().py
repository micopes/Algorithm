import heapq

def solution(food_times, k):
    answer = -1
    
    h = []
    for i in range(len(food_times)):
        heapq.heappush(h, (food_times[i], i+1)) # 1번부터 시작.
    
    prev_val = 0
    length = len(food_times)
    
    
    while h:
        t = (h[0][0] - prev_val) * length
        if k >= t:
            k -= t
            prev_val, _ = heapq.heappop(h)
            length -= 1
        else:
            idx = k % length
            h.sort(key = lambda x : x[1])
            answer = h[idx][1]
            break
        
    return answer
    
    
        
    
    
    