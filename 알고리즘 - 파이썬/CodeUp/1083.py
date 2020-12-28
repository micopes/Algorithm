n = int(input())

for i in range(1, n+1):
    if i % 3 == 0:
        print("X ", end = "")
    else :
        print("%d " % i, end = "")