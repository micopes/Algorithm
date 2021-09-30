import sys
import heapq
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    
    n = int(input().rstrip())
    numbers = []
    for i in range(n // 10 + 1):
        numbers.extend(list(map(int, input().rstrip().split())))

    
    heap = []
    ans_list = []
    for i in range(0, len(numbers)):
        temp_list = []
        heapq.heappush(heap, numbers[i])
        # index가 짝수일때 홀수번째.
        if i % 2 == 0:
            for j in range(i // 2):
                temp_list.append(heapq.heappop(heap))
            
            ans_list.append(heap[0])
            
            for j in range(i // 2):
                heapq.heappush(heap, temp_list[j])
        
    
    print(len(ans_list))
    cnt = len(ans_list) // 10
    for i in range(cnt):
        for j in range(i*10, (i+1)*10):
            print(ans_list[j], end = " ")
        print()
        
    for i in range(10*cnt, len(ans_list)):
        print(ans_list[i], end = " ")
        
            
            
            
            