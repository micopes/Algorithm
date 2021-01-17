import sys
input = sys.stdin.readline

n = int(input().strip())
sang = list(map(int, input().strip().split()))
sang.sort()
m = int(input().strip())
cards = list(map(int, input().strip().split()))

for card in cards:
    start, end = 0, n-1
    flag = 0
    while start <= end:
        mid = (start + end) // 2
        
        if sang[mid] == card:
            flag = 1
            break
        elif sang[mid] >= card:
            end = mid - 1
        else:
            start = mid + 1
    print("%d" % flag, end = " ")
    


