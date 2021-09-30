import sys
input = sys.stdin.readline

numbers = list(map(int, input().rstrip().split()))

numbers.sort()

# 같은 눈 3개

ans = 0

if numbers[0] == numbers[1] and numbers[1] == numbers[2]:
    ans = 10000 + numbers[0]*1000
elif numbers[0] == numbers[1]:
    ans = 1000 + numbers[1]*100
elif numbers[1] == numbers[2]:
    ans = 1000 + numbers[1]*100
else:
    ans = numbers[2]*100

print(ans)
