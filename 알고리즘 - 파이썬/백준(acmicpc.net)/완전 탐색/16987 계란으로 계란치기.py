import sys
# input = sys.stdin.readline

def backtrack(idx, d_list, w_list, cnt):
    global max_cnt

    if cnt > max_cnt:
        max_cnt = cnt
        # 가장 오른쪽에 위치한 계란도 이용한 경우
        
    if idx == n:
        return
    # 손에 계란이 깨진 경우
    if d_list[idx] <= 0:
        backtrack(idx+1, d_list, w_list, cnt)
    else:
        # idx와 또 하나의 계란의 충돌
        for i in range(n):
            # 또 하나의 계란이 자기 자신인 경우 넘기기
            if i == idx:
                continue
            # 다음 계란이 깨지지 않은 경우
            if d_list[i] > 0:
                d_list[idx] -= w_list[i]
                d_list[i] -= w_list[idx]
               
                # 깨진 cnt 추가
                temp_cnt = cnt
                if d_list[idx] <= 0:
                    temp_cnt += 1
                if d_list[i] <= 0:
                    temp_cnt += 1
                
                backtrack(idx+1, d_list, w_list, temp_cnt)
                
                # 다음 상황을 위해 되돌리기
                d_list[idx] += w_list[i]
                d_list[i] += w_list[idx]
        
    

n = int(input().rstrip())

d_list = [] # 내구도
w_list = [] # 무게

for _ in range(n):
    # d : 내구도, w : 무게
    d, w = map(int, input().rstrip().split())
    d_list.append(d)
    w_list.append(w)

# idx, d_list, w_list, cnt
max_cnt = 0
backtrack(0, d_list, w_list, 0)

print(max_cnt)


