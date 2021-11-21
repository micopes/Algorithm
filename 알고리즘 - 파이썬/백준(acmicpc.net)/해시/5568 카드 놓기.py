import sys
from itertools import permutations
# input = sys.stdin.readline


n = int(input().rstrip())
k = int(input().rstrip())

card = []
for _ in range(n):
    x = input().rstrip()
    card.append(x)
    
integer = set()
for x in permutations(card, k):
    x = list(x)
    integer.add("".join(x))

print(len(integer))

