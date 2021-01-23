import sys
# input = sys.stdin.readline

string = input().strip()

Ball = [1, 0, 0]

for i in range(len(string)):
    if string[i] == 'A':
        Ball[0], Ball[1] = Ball[1], Ball[0]
    elif string[i] == 'B':
        Ball[1], Ball[2] = Ball[2], Ball[1]
    elif string[i] == 'C':
        Ball[0], Ball[2] = Ball[2], Ball[0]

for i in range(3):
    if Ball[i] == 1:
        print(i+1)
