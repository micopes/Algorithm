n = int(input())
k = n-2

for i in range(n-1):
    print(" ", end = "")
if n != 1:
    print("*")

for i in range(k): 
    for j in range(k-i):
        print(" ", end = "")
    print("*", end = "")
    for j in range(2*(i+1)-1):
        print(" ", end = "")
    print("*")

for i in range(2*n-1):
    print("*", end = "")
        
    