n = int(input(), 16)

for i in range(1, 16) :
    k = n * i    
    
    print("%X*%X=%X" %(n, i, k))