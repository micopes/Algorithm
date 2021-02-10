import sys
# input = sys.stdin.readline

idx = 1
while True:
    L, P, V = map(int, input().rstrip().split())
    result = 0
    if L == 0 and P == 0 and V == 0:
        break
    result += (V//P)*L
    result += min(V%P, L)
    print("Case %d: %d" % (idx, result))
    idx += 1