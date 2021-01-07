n = int(input())

card = [0 for _ in range(n)] # 0 ~ 99999

for i in range(n):
    x = int(input())
    card[i] = x

card.sort()

seq = [0 for _ in range(n)]
for i in range(n):
    if i == 0:
        seq[i] = 1
    else:
        if card[i] == card[i-1]:
            seq[i] = seq[i-1] + 1
        else:
            seq[i] = 1

maxVal = max(seq) 
# maxVal는 아마 전체 O(N)일것이라서 max(seq)로 밑에 넣어주면 O(N^2)이 되어 시간초과.
for i in range(n):
    if maxVal == seq[i]:
        print(card[i])
        break
