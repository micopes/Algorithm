import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

total = []
a = []
b = []
a = list(map(int, input().strip().split()))
b = list(map(int, input().strip().split()))
total = a + b
total.sort()

for i in total:
    print(i, end = " ")    
# 정렬되어있는 것을 이용하지 않으려면 굳이 입력을 따로 받을 필요가 없다.