import sys
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    dic = {}
    for i in range(n):
        item, key = input().rstrip().split()
        if key not in dic:
            dic[key] = 1
        else:
            dic[key] += 1
    
    ans = 1
    for x in dic.values():
        ans *= (x+1) # 2개가 있다고 치면 -> 없는것, 1번째, 2번째 이렇게 해서 3개.
    print(ans - 1)