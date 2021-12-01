import sys
# input = sys.stdin.readline

def mul(matrix1, matrix2):
    ret_matrix = [[0]*n for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            for k in range(n):
                ret_matrix[i][j] += matrix1[i][k]*matrix2[k][j]
                ret_matrix[i][j] %= 1000
    return ret_matrix

def divide(matrix, b):
    if b == 1:
        return matrix
    elif b == 2:
        return mul(matrix, matrix)
    else:
        tmp = divide(matrix, b//2)
        if b % 2 == 0:
            return mul(tmp, tmp)
        else:
            return mul(mul(tmp, tmp), matrix)
            

n, b = map(int, input().rstrip().split())
matrix = []

for _ in range(n):
    matrix.append(list(map(int, input().rstrip().split())))

res_matrix = divide(matrix, b)

for i in range(n):
    for j in range(n):
        print(res_matrix[i][j] % 1000, end = " ")
    print()