import sys
import copy # deepcopy를 위함
# input = sys.stdin.readline

def check(li):
    global ans
    # 가로
    prev_chr = li[0][0]
    
    for i in range(n):
        prev = 1
        for j in range(n-1):
            if li[i][j] == li[i][j+1]:
                prev_chr = li[i][j+1]
                prev += 1
                if prev > ans:
                    ans = prev
            else:
                prev = 1
        
    for i in range(n):
        prev = 1
        for j in range(n-1):
            if li[j][i] == li[j+1][i]:
                prev_chr = li[j+1][i]
                prev += 1
                if prev > ans:
                    ans = prev
            else:
                prev = 1
                

# 입력
n = int(input()) 

board = []

for i in range(n):
    string = input()
    board.append(list(string))

# 결과값
ans = 1

# 가로
for i in range(n):
    for j in range(n-1):
        temp_list = copy.deepcopy(board)
        # swap
        temp = temp_list[i][j]
        temp_list[i][j] = temp_list[i][j+1]
        temp_list[i][j+1] = temp
        
        check(temp_list)

# 세로
for i in range(n):
    for j in range(n-1):
        temp_list = copy.deepcopy(board)
        # swap
        temp = temp_list[j][i]
        temp_list[j][i] = temp_list[j+1][i]
        temp_list[j+1][i] = temp
        
        check(temp_list)
    
print(ans)

