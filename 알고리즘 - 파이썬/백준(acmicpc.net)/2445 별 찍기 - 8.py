n = int(input())

for i in range(1, n+1):
    for j in range(1, i+1):
        print('*', end = "")
    for j in range(2*(n-i)):
        print(' ', end = "")
    for j in range(1, i+1):
        print('*', end = "")
    print()

for i in range(n-1, 0, -1):
    for j in range(1, i+1):
        print('*', end = "")
    for j in range(2*(n-i)):
        print(' ', end = "")
    for j in range(1, i+1):
        print('*', end = "")
    print()
    


# 별 1 2 3 4 5 

# 빈 8 6 4 2 0 

# 별 1 2 3 4 5 

# 4 3 2 1

# 2 4 6 8

# 4 3 2 1