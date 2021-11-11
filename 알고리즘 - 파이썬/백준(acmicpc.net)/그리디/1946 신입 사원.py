import sys
# input = sys.stdin.readline

T = int(input().rstrip())

for _ in range(T):
    n = int(input().rstrip())
    
    arr = []
    for i in range(n):
        docu, inte = map(int, input().rstrip().split())
        arr.append([docu, inte])
        
    arr.sort()
    cnt = 1
    # 순위
    rank = arr[0][1]
    
    for i in range(1, n):
        if rank > arr[i][1]:
            rank = arr[i][1]
            cnt += 1
    print(cnt)
            