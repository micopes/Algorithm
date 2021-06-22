import heapq

def solution(scoville, K):
    answer = 0
    
    heap = []
    for i in range(len(scoville)):
        heapq.heappush(heap, scoville[i])
    try: # heap안의 원소가 2개 미만으로 떨어질 수 있다. 그러면 K 이상으로 만들 수 없기 때문에 -1을 리턴하면 된다.
        while heap[0] < K:
            answer += 1
            a = heapq.heappop(heap)
            b = heapq.heappop(heap)
            temp = a + b*2
            heapq.heappush(heap, temp)
    except:
        answer = -1
        
    
    return answer