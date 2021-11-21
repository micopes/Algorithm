import sys
# input = sys.stdin.readline

# 저장된 사이트의 수 / 비밀번호를 찾으려는 사이트 주소의 수
dic = {}

n, m = map(int, input().rstrip().split())

for i in range(n):
    site, val = input().rstrip().split()
    dic[site] = val

for _ in range(m):
    x = input().rstrip()
    print(dic[x])