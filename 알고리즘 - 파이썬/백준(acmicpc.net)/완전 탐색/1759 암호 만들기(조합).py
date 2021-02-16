from itertools import combinations

r, n = map(int, input().rstrip().split())
arr = list(input().rstrip().split())
arr.sort()

nCr = combinations(arr, r)
data = list(nCr)
for i in range(len(data)):
    tempList = data[i]
    mo = 0
    za = 0
    for ch in tempList:
        if ch in ['a', 'e', 'i', 'o', 'u'] :
            mo += 1
        else:
            za += 1
    if mo >= 1 and za >= 2:
        print("".join(tempList))