def rotation(key):
    n = len(key)
    result = [[0]*n for _ in range(n)]
    # 90도 회전
    for i in range(n):
        for j in range(n):
            result[i][j] = key[j][n-1-i]
    return result

def check(new_lock):
    length = len(new_lock)//3
    
    for i in range(length, length*2):
        for j in range(length, length*2):
            if new_lock[i][j] != 1:
                return False
    return True

def solution(key, lock):
    answer = False
    n = len(lock)
    m = len(key)
    
    new_lock = [[0]*(n*3) for _ in range(n*3)]
    
    # 중앙 채우기
    for i in range(n):
        for j in range(n):
            new_lock[n+i][n+j] = lock[i][j]
    
    for _ in range(4):
        key = rotation(key)
        for x in range(2*n):
            for y in range(2*n):
                # 열쇠 넣기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] += key[i][j]
                # 검사
                if check(new_lock) == True:
                    return True
            
                # 열쇠 빼기
                for i in range(m):
                    for j in range(m):
                        new_lock[x+i][y+j] -= key[i][j]
    return False