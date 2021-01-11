n, m = map(int, input().split())

fives = []
twos = []

i = 5
while i <= 2000000000:
    fives.append(i)
    i = i * 5
    
i = 2
while i <= 2000000000:
    twos.append(i)
    i = i * 2

two1 = 0 # m!의 끝자리 0의 개수
two2 = 0 # (m-n)! + n!의 끝자리 0의 개수
five1 = 0
five2 = 0

for i in range(len(twos)):
    if n < twos[i]:
        break
    two1 += n // twos[i]
for i in range(len(twos)):
    if (n-m) < twos[i]:
        break
    two2 += (n-m) // twos[i]
for i in range(len(twos)):
    if m < twos[i]:
        break
    two2 += m // twos[i]

    
for i in range(len(fives)):
    if n < fives[i]:
        break
    five1 += n // fives[i]
for i in range(len(fives)):
    if (n-m) < fives[i]:
        break
    five2 += (n-m) // fives[i]
for i in range(len(fives)):
    if m < fives[i]:
        break
    five2 += m // fives[i]


result = min(two1-two2, five1-five2)
print(result)
    