n, b = map(int, input().split())

res = []
while n :
    val = n % b
    if val >= 10:
        val -= 10
        val = val + ord('A')
        res.append(chr(val))
    else:
        res.append(val)
    n = n // b

res.reverse()
for i in range(len(res)):
    print(res[i], end = "")