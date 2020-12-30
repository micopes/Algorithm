n = int(input())


for i in range(n) : # i : 0 1 2 3 4
    # 빈 0 1 2 3 4
    for j in range(i):
        print(" ", end = "")
    # 별 9 7 5 3 1
    for j in range(2*(n-i)-1):
        print("*", end = "")
    print()     
    
    
for i in range(n-1): # i : 0 1 2 3
    # 빈 3 2 1 0
    for j in range(n-2-i):
        print(" ", end = "")    
    # 별 3 5 7 9
    for j in range(2*(i+1)+1):
        print("*", end = "")
    print()





