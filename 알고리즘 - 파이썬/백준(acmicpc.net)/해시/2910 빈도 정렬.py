import sys
# input = sys.stdin.readline

# 자주 등장하는 빈도 순으로 정렬 (빈도가 높을 수록 앞에, 등장한 횟수가 같다면 먼저 나온 것이 앞에.

N, C = map(int, input().rstrip().split())
# list로 하면 index가 1,000,000,000까지 가야하므로 딕셔너리를 사용한다.
message = list(map(int, input().rstrip().split()))

dic = {}
dic_count = {}
cnt = 0

for x in message:
    if x in dic:
        dic[x] += 1
    else:
        dic[x] = 1
        dic_count[x] = cnt
        cnt += 1

# dic에 해당 키의 빈도
# dic_count에 먼저 나온 것. (cnt가 낮을수록 먼저 나온 것.) 

# [key, 빈도, 먼저 나온 것]
temp_list = []
for key in dic.keys():
    temp_list.append((key, dic[key], dic_count[key]))
    
temp_list.sort(key = lambda x : (-x[1], x[2]))

for k in temp_list:
    key = k[0]
    freq = k[1]
    for _ in range(freq):
        print(key, end = " ")
    
    
    
    
        
        
    