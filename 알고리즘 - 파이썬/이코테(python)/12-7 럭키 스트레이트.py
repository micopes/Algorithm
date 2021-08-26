import sys
input = sys.stdin.readline

string = input()
length = len(string)//2

left = int(string[0:length])
right = int(string[length:])

left_sum = 0
right_sum = 0

while left:
    left_sum += left % 10
    left = left // 10

while right:
    right_sum += right % 10
    right = right // 10

if left_sum == right_sum:
    print('LUCKY')
else:
    print('READY')
    
    
