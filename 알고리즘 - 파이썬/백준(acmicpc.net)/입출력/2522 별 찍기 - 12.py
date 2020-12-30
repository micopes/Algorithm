n = int(input())

for i in range(n): # 0 1 2
    # 빈 2 1 0
    for j in range(n-i-1):
        print(' ', end = "")
    # 별 1 2 3        
    for j in range(i+1):
        print('*', end = "")
    print()

for i in range(n-1): # 0 1
    # 빈 1 2
    for j in range(i+1):
        print(' ', end = "")
    # 별 2 1    
    for j in range(n-i-1):
        print('*', end = "")
    print()
    




