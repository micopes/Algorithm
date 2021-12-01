import sys
# input = sys.stdin.readline

a_row, a_col = map(int, input().rstrip().split())
a_matrix = []

for _ in range(a_row):
    a_matrix.append(list(map(int, input().rstrip().split())))

b_row, b_col = map(int, input().rstrip().split())
b_matrix = []

for _ in range(b_row):
    b_matrix.append(list(map(int, input().rstrip().split())))

ans_matrix = [[0]*b_col for _ in range(a_row)]
for i in range(a_row):
    for j in range(b_col):
        # a_col or b_row
        for k in range(a_col):
            ans_matrix[i][j] += a_matrix[i][k]*b_matrix[k][j]
            
for i in range(len(ans_matrix)):
    for j in range(len(ans_matrix[0])):
        print(ans_matrix[i][j], end = " ")
    print()
    
            
    



    
    
    