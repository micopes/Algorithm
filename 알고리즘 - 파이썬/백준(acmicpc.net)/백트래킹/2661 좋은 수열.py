import sys
# input = sys.stdin.readline

def check(string):
    temp = string[::-1]
    for i in range(2, len(string)+1):
        left = temp[:i//2]
        right = temp[i//2:i//2*2]
        if left == right:
            return False
    return True

def backtrack(string):
    if len(string) == n:
        # 모든 경우의 수를 다 하면 시간 초과 - (1, 2, 3) 순서대로 백트래킹하니까 맨처음에 나오는 것이 가장 작은 숫자
        print(string)
        sys.exit(0)
        return

    for x in ('1', '2', '3'):
        temp = string + x
        if check(temp):
            backtrack(temp)
        
    
n = int(input().rstrip())

li = []
string = ""
backtrack(string)