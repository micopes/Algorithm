import sys
# input = sys.stdin.readline

student = [[0]*7 for _ in range(2)]

n, k = map(int, input().rstrip().split())

for i in range(n):
    # sex : 0, 1
    # grade : 1 ~ 6
    sex, grade = map(int, input().rstrip().split())
    student[sex][grade] += 1

room = 0

for i in range(2):
    for j in range(1, 7):
        room += student[i][j] // k
        if student[i][j] % k != 0:
            room += 1

print(room)