sum = 0
n, m, k = map(int, input().split())
data = list(map(int, input().split()))

data.sort()

first = data[n-1]
second = data[n-2]

for i in range(m) :
    if i % (k+1) == k :
        sum += second
    else :
        sum += first
        
print(sum)