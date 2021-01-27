import sys
# input = sys.stdin.readline

n = int(input().strip())
schedule = []
for i in range(n):
    x, y = map(int, input().strip().split())
    if i >= 1 and x < schedule[-1][0] and y > schedule[-1][1]:
        continue
    schedule.append([x, y])

# 빨리 끝나는 기준으로 정렬 후 시작 빠른 것 순.
schedule.sort(key = lambda x : (x[1], x[0]))
    

now = 0
result = 0
for i in range(len(schedule)):
    start, end = schedule[i][0], schedule[i][1]
    if now <= start:
        result += 1
        now = end
        
print(result)
        

            
    

