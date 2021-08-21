import sys
# input = sys.stdin.readline

n = int(input().rstrip())
ant_list = list(map(int, input().rstrip().split()))

ant_list.sort()

print(ant_list[n//2]-1) # 중간 값. 짝수 개라서 중간값이 2개인 경우에는 그 중간값을 선택하지 않고 가장 index 작은 값 선택