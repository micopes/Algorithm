import sys
input = sys.stdin.readline

def check(arr):
    idx = 0
    cur_level = arr[idx]
    build = [0]*n
    
    while idx < n-1:
        prev_level = cur_level
        idx += 1
        cur_level = arr[idx]
        
        # 같은 경우
        if prev_level == cur_level:
            continue
        
        # 차이가 2 이상 나서 경사로를 설치할 수 없는 경우
        elif abs(prev_level - cur_level) > 1:
            return 0
        
        # 내려가는 경우
        elif prev_level == cur_level + 1:
            # 설치할 공간이 없는 경우
            if idx + l > n:
                return 0
        
            for i in range(l):
                # 경사 아래와 같고, 경사가 설치된 적 없는 경
                if cur_level == arr[idx+i] and build[idx+i] == 0:
                    build[idx+i] = 1
                    continue
                else:
                    return 0
        # 올라가는 경우
        elif prev_level == cur_level - 1:
            if idx < l:
                return 0
        
            for i in range(l):
                if prev_level == arr[idx-1-i] and build[idx-1-i] == 0:
                    build[idx-1-i] = 1
                    continue
                else:
                    return 0
    
    return 1
                    
                
            

n, l = map(int, input().rstrip().split())
board = []

for i in range(n):
    temp_list = list(map(int, input().rstrip().split()))
    board.append(temp_list)

cnt = 0
for i in range(n):
    cnt += check(board[i])
    cnt += check([k[i] for k in board])

print(cnt)