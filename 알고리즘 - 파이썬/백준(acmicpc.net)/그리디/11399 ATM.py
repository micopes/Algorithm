import sys
input = sys.stdin.readline

n = int(input().strip())
man = list(map(int, input().strip().split()))

man.sort()

result = 0
_sum = 0 # 이때까지의 sum
for i in man:
    _sum += i
    result += _sum

print(result)
    
    
    