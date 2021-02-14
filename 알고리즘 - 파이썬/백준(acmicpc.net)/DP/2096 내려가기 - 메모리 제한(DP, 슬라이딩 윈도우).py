import sys
# input = sys.stdin.readline

n = int(input().rstrip())

box = []
for i in range(n):
    box.append(list(map(int, input().rstrip().split())))
   
dp1 = [0, 0, 0]
dp2 = [0, 0, 0]

dp1[0] = dp2[0] = box[0][0]
dp1[1] = dp2[1] = box[0][1]
dp1[2] = dp2[2] = box[0][2]

for i in range(1, n):
    dp1[0], dp1[1], dp1[2] = max(dp1[0], dp1[1]) + box[i][0],\
        max(dp1[0], dp1[1], dp1[2]) + box[i][1],\
        max(dp1[1], dp1[2]) + box[i][2]
    
    dp2[0], dp2[1], dp2[2] = min(dp2[0], dp2[1]) + box[i][0],\
        min(dp2[0], dp2[1], dp2[2]) + box[i][1],\
        min(dp2[1], dp2[2]) + box[i][2]

print(max(dp1), min(dp2))
