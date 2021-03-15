import sys
# input = sys.stdin.readline

hour, minute, second = 0, 0, 0
h = int(input().rstrip())

ans = 0
while True:
    second += 1    
    if second % 10 == 3 or second // 10 == 3 or\
        minute % 10 == 3 or minute // 10 == 3 or\
            hour % 10 == 3:
                ans += 1
    if second == 60:
        second = 0
        minute += 1
    if minute == 60:
        minute = 0
        hour += 1
    if hour == h+1:
        break

print(ans)