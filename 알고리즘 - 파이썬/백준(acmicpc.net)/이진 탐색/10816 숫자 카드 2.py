import sys
# input = sys.stdin.readline

n = int(input().strip())
sang = list(map(int, input().strip().split()))
m = int(input().strip())
cards = list(map(int, input().strip().split()))

sang.sort()

cardCount = [0 for _ in range(20000001)]
for data in sang:
    cardCount[data+10000000] += 1

for card in cards:
    flag = 0
    start, end = 0, n-1
    while start <= end:
        mid = (start + end) // 2
        if sang[mid] == card:
            flag = 1
            break
        elif sang[mid] > card:
            end = mid - 1
        else:
            start = mid + 1
    if flag == 1:
        print("%d" % cardCount[card+10000000], end = " ")
    else:
        print("%d" % 0, end = " ")
    

