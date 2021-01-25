import sys
input = sys.stdin.readline

string = input().strip()
data = []
for i in string:
    data.append(int(i))

data.sort(reverse = True)
result = data[:]
if data[-1] != 0:
    print(-1)
    data.pop()
else:
    sum_ = 0
    for i in data:
        sum_ += i
    
    if sum_ % 3 == 0:
        for i in result:
            print(i, end = "")
    else:
        print(-1)