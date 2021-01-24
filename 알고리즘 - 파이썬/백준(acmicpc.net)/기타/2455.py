import sys
input = sys.stdin.readline
result = 0
total = 0
for i in range(4):
    train_out, train_in = map(int, input().strip().split())
    total -= train_out
    total += train_in
    result = max(total, result)

print(result)