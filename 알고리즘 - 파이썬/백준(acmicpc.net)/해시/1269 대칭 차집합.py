import sys
input = sys.stdin.readline

a_num, b_num = map(int, input().rstrip().split())

a_list = set(map(int, input().rstrip().split()))
b_list = set(map(int, input().rstrip().split()))

print(len(a_list - b_list) + len(b_list - a_list))